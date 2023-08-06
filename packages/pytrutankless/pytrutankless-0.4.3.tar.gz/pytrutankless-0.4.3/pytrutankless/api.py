from __future__ import annotations
from datetime import datetime, timezone

import logging
from typing import Dict, Optional

from aiohttp import ClientSession


from .device import Device
from .token import Token

_LOGGER = logging.getLogger(__name__)


BASE_URL = "https://home.trutankless.com/"
DEVICES_URL = f"{BASE_URL}api/dashboard/devices/"
LOCATIONS_URL = f"{BASE_URL}api/dashboard/locations"
TOKEN_URL = f"{BASE_URL}api/dash-oauth/token"
CLIENT_ID = "123"
GRANT_TYPE = "password"
HEADERS = {"Content-Type": "application/json"}


async def get_token(
    session: ClientSession,
    username: str,
    password: str,
    client_id: str = CLIENT_ID,
    grant: str = GRANT_TYPE,
) -> Token:
    """Retrieve token from the API."""
    payload = {
        "username": username,
        "password": password,
        "grant_type": grant,
        "client_id": client_id,
    }

    async with session.post(TOKEN_URL, data=payload) as _token_resp:
        new_token = await Token.from_dict(await _token_resp.json())
    HEADERS["Authorization"] = f"Bearer {new_token.access_token}"
    return new_token


async def refresh_token(session: ClientSession, token: Token) -> Token:
    """Obtain new access token using the refresh token."""
    ref_tok = token.ref_tok
    payload = {
        "client_id": CLIENT_ID,
        "grant_type": "refresh_token",
        "refresh_token": ref_tok,
    }

    async with session.post(TOKEN_URL, data=payload) as _refresh_resp:
        _response = await _refresh_resp.json()
        token.access_token = _response["access_token"]
        HEADERS["Authorization"] = f"Bearer {token.access_token}"
        return token


class TruTanklessApiInterface:
    """Interface to TruTankless API."""

    def __init__(
        self,
        user: str,
        passwd: str,
        token: Optional[Token] = None,
    ) -> None:
        """Create the TruTankless API interface object."""
        self._headers: dict = HEADERS
        self._location_id: str
        self._user_id: str
        self._locations: Dict = {}
        self._user = user
        self._passwd = passwd
        self.devices: Dict = {}
        self.session = ClientSession()
        self.token = token

    async def authenticate(self) -> Token:
        """Return valid access token."""
        if self.token and self.token.expires_at > datetime.now(timezone.utc):
            return self.token
        if self.token and self.token.expires_at < datetime.now(timezone.utc):
            _LOGGER.debug("access token is expired. Refreshing access token.")
            return await refresh_token(self.session, self.token)
        self.token = await get_token(
            self.session, username=self._user, password=self._passwd
        )
        HEADERS["Authorization"] = f"Bearer {self.token.access_token}"
        return self.token

    async def get_devices(self):
        """Get a list of all the devices for this user and instantiate device objects."""
        await self._get_locations()
        for _devlist in self._locations[0]["devices"]:
            _dev_obj = Device(_devlist, self)
            self.devices[_dev_obj.device_id] = _dev_obj
        return self.devices

    async def refresh_device(self, device: str):
        """Fetch updated data for a device."""
        _device_url = f"{DEVICES_URL}{device}"
        async with self.session.get(
            _device_url, headers=self._headers
        ) as refr:
            _refdata = await refr.json()
            _LOGGER.debug("Retrieved updated data from API: %s", _refdata)
            dev_obj = self.devices.get(_refdata.get("id", ""), None)
            if dev_obj:
                await dev_obj.update_device_info(_refdata)
        return dev_obj

    async def _get_locations(self) -> None:
        async with self.session.get(
            LOCATIONS_URL, headers=self._headers
        ) as resp:
            if resp.status == 200:
                self._locations = await resp.json()
                _LOGGER.debug(self._locations)

    @property
    def user_id(self) -> str:
        """Return the user id."""
        return self._user_id
