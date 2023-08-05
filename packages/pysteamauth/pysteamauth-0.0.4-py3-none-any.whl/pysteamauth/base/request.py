from typing import (
    Any,
    Dict,
    Mapping,
    Optional,
    Type,
)

import aiohttp
from aiohttp import (
    ClientResponse,
    ClientResponseError,
    ClientSession,
)

from pysteamauth.abstract import RequestStrategyAbstract
from pysteamauth.errors import check_steam_error
from pysteamauth.errors.exceptions import (
    TooManySteamRequestsError,
    UnauthorizedSteamRequestError,
)


class BaseRequestStrategy(RequestStrategyAbstract):

    http_status_exception: Dict[int, Type[Exception]] = {
        401: UnauthorizedSteamRequestError,
        429: TooManySteamRequestsError,
    }

    def __init__(self):
        self._session: Optional[ClientSession] = None

    def __del__(self):
        if self._session:
            self._session.connector.close()

    def _create_session(self) -> ClientSession:
        """
        Create aiohttp session.
        Aiohttp session saves and stores cookies.
        It writes cookies from responses after each request that specified
        in Set-Cookie header.

        :return: aiohttp.ClientSession object.
        """
        return ClientSession(connector=aiohttp.TCPConnector(ssl=False))

    def _check_http_status(self, response: ClientResponse) -> None:
        try:
            response.raise_for_status()
        except ClientResponseError as error:
            if error.status in self.http_status_exception:
                raise self.http_status_exception[error.status](
                    f'Wrong HTTP status from Steam {error.status} url="{response.url}"',
                )

    async def request(self, url: str, method: str, **kwargs: Any) -> ClientResponse:
        if self._session is None:
            self._session = self._create_session()
        response = await self._session.request(method, url, **kwargs)
        error = response.headers.get('X-eresult')
        if error:
            check_steam_error(int(error))
        self._check_http_status(response)
        return response

    def cookies(self, domain: str = 'steamcommunity.com') -> Mapping[str, str]:
        if self._session is None:
            raise RuntimeError('Session is not initialized')
        cookies = {}
        for cookie in self._session.cookie_jar:
            if cookie['domain'] == domain:
                cookies[cookie.key] = cookie.value
        return cookies

    async def text(self, url: str, method: str, **kwargs: Any) -> str:
        return await (await self.request(url, method, **kwargs)).text()

    async def bytes(self, url: str, method: str, **kwargs: Any) -> bytes:
        return await (await self.request(url, method, **kwargs)).read()
