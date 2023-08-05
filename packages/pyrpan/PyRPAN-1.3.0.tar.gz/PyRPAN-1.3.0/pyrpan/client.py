import asyncio
import logging
from typing import Optional

import aiohttp
import asyncpraw
from expiringdict import ExpiringDict

from .exceptions import APIError, InvalidRequest, RateLimitExceeded
from .models import Broadcast, Broadcasts

logger = logging.getLogger(__name__)


class PyRPAN:
    """
    Client class for the PyRPAN API Wrapper.
    Attributes
    ----------
    reddit : str
        The Reddit instance to use to access the Reddit API.
    top_broadcasts_cache : ExpiringDict
        A cache of the top broadcasts.
    api_url : str
        URL to access the RPAN API.
    session : aiohttp.ClientSession
        For creating client session and to make requests.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        """
        Construct the PyRPAN wrapper.

        Parameters
        ----------
        client_id : str
            Client ID generated from creating an app at https://old.reddit.com/prefs/apps/.
        client_secret : str
            Client Secret generated from creating an app at https://old.reddit.com/prefs/apps/.
        """
        self.api_url = "https://strapi.reddit.com"
        self.top_broadcasts_cache = ExpiringDict(max_len=3, max_age_seconds=300)
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = "Reddit Public Access Network (RPAN) API Wrapper by b1uejay27."
        self._session = None
        self._lock = asyncio.Lock()

    async def close(self) -> None:
        """Close the client session."""
        if self._session is not None:
            await self._session.close()

    async def fetch(
        self, method: str, route: str, *, headers: Optional[dict] = None, data: Optional[dict] = None
    ) -> Optional[dict]:
        """
        Fetching a response from the API
        Parameters
        ----------
        route : str
            The API route you want to make a call to
        headers : dict
            Headers for the API call, Defaults to None
        data : dict
            Data for the API call, Defaults to None
        Returns
        -------
        Optional[dict]
            The response from the API.
        """
        if headers is None:
            headers = {}

        headers = {
            "User-Agent": "Reddit Public Access Network (RPAN) API Wrapper by b1uejay27.",
            "Cache-Control": "no-cache",
            **headers,
        }

        if not self._session:
            self._session = aiohttp.ClientSession()

        async with self._lock:
            async with self._session.request(
                method=method, url=self.api_url + route, headers=headers, data=data
            ) as res:
                # Handle status codes
                if res.status in [200, 201, 204]:
                    data = await res.json()

                elif res.status == 404:
                    raise InvalidRequest("The requested resource was not found.")

                elif res.status == 429:
                    raise RateLimitExceeded("Too many requests - Slow down your requests.")

                elif res.status == 500:
                    raise APIError("The RPAN API seems to be having some issues at the moment, please try again later.")

        return data

    async def get_viewer_subreddits(self) -> list:
        """
        Gets a list of the recommended viewer RPAN subreddits.

        Returns
        -------
        list
            The list of viewer subreddits.
        """
        data = await self.fetch(method="GET", route="/recommended_viewer_subreddits")
        return data["data"]

    async def get_broadcast(self, id: str) -> Broadcast:
        """
        Gets a broadcast by ID.

        Parameters
        ----------
        id : str
            ID of the broadcast you want to fetch.
        Returns
        -------
        Broadcast
            The retrived broadcast or None.
        """
        data = await self.fetch(method="GET", route=f"/broadcasts/{id}")
        payload = data["data"]

        return Broadcast(payload=payload)

    async def get_broadcasts(self) -> Broadcasts:
        """
        Fetches all the currently active broadcasts.

        Returns
        -------
        Broadcasts
            The retrived broadcasts or None.
        """
        data = await self.fetch(method="GET", route="/broadcasts")

        broadcasts = []
        if len(data["data"]):
            for broadcast in data["data"]:
                payload = broadcast
                broadcasts.append(Broadcast(payload=payload))

            return Broadcasts(contents=broadcasts)

    async def get_last_broadcast(self, username: str) -> Optional[Broadcast]:
        """
        Gets the last broadcast of a user.

        Parameters
        ----------
        username : str
            The username of the user you want to get the last broadcast for.

        Returns
        -------
        Broadcast
            The found last broadcast or None.
        """
        async with asyncpraw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.user_agent,
        ) as reddit:
            user = await reddit.redditor(username)
            async for submission in user.submissions.new(limit=25):
                if self.is_rpan_broadcast(submission.url):
                    broadcast = await self.get_broadcast(id=submission.id)
                    return broadcast
            return None

    def is_rpan_broadcast(self, link: str) -> bool:
        """
        Checks if a link is a valid RPAN broadcast.

        Parameters
        ----------
        link : str
            The link to check.

        Returns
        -------
        bool
            If the link is a valid RPAN broadcast.
        """
        if "reddit.com/rpan/" in link:
            return True
        else:
            return False
