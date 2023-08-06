"""Low-level API for interacting with Imou devices."""
import hashlib
import logging
import random
import secrets
import time
from datetime import datetime, timedelta

from aiohttp import ClientSession

from imouapi.const import API_URL, DEFAULT_TIMEOUT
from imouapi.exceptions import (
    APIError,
    ConnectionFailed,
    InvalidConfiguration,
    InvalidResponse,
    NotAuthorized,
    NotConnected,
)

_LOGGER = logging.getLogger(__package__)


class ImouAPIClient:
    """Interact with IMOU API."""

    def __init__(
        self,
        app_id: str,
        app_secret: str,
        websession: ClientSession,
        base_url: str = None,
        timeout: int = None,
    ) -> None:
        """
        Initialize the instance.

        Parameters:
            base_url: base url for API calls (e.g. https://openapi.easy4ip.com/openapi)
            app_id: appID from https://open.imoulife.com/consoleNew/myApp/appInfo
            app_secret: appID from https://open.imoulife.com/consoleNew/myApp/appInfo
            websession: aiohttp client session
        """
        self.log_http_requests = True
        self._websession = websession
        self._base_url = base_url if base_url is not None else API_URL
        self._app_secret = app_secret
        self._app_id = app_id
        self._access_token = None
        self._access_token_expire_time = None
        self._connected = False
        self._timeout = timeout if timeout is not None else DEFAULT_TIMEOUT
        _LOGGER.debug("Initialized. Endpoint URL: %s", self._base_url)

    async def async_connect(self) -> bool:
        """Authenticate against the API and retrieve an access token."""
        # check if we already have an access token and if so assume already authenticated
        if self.is_connected():
            return True
        # call the access token endpoint
        _LOGGER.debug("Connecting")
        data = await self._async_call_api("accessToken", {}, True)
        if "accessToken" not in data or "expireTime" not in data:
            raise InvalidResponse(f"accessToken not found in {data}")
        # store the access token
        self._access_token = data["accessToken"]
        self._access_token_expire_time = data["expireTime"]
        _LOGGER.debug("Retrieved access token: %s", self._access_token)
        self._connected = True
        _LOGGER.debug("Connected succesfully")
        return True

    async def async_disconnect(self) -> bool:
        """Disconnect from the API."""
        self._access_token = None
        self._access_token_expire_time = None
        self._connected = False
        _LOGGER.debug("Disconnected")
        return True

    def is_connected(self) -> bool:
        """Return true if already connected."""
        return self._connected

    async def async_reconnect(self) -> bool:
        """Reconnect to the API."""
        await self.async_disconnect()
        return await self.async_connect()

    async def _async_call_api(self, api: str, payload: dict, is_connect_request: bool = False) -> dict:
        """Submit request to the HTTP API endpoint."""
        # if this is not a connect request, check if we are already connected
        if not is_connect_request:
            if not self.is_connected():
                raise NotConnected()

        # calculate timestamp, nonce, sign and id as per https://open.imoulife.com/book/http/develop.html
        timestamp = round(time.time())
        nonce = secrets.token_urlsafe()
        sign = hashlib.md5(f"time:{timestamp},nonce:{nonce},appSecret:{self._app_secret}".encode("utf-8")).hexdigest()
        request_id = str(random.randint(1, 10000))

        # add the access token to the payload if already available
        if self._access_token is not None:
            payload["token"] = self._access_token

        # prepare the API request
        url = f"{self._base_url}/{api}"
        body = {
            "system": {
                "ver": "1.0",
                "sign": sign,
                "appId": self._app_id,
                "time": timestamp,
                "nonce": nonce,
            },
            "params": payload,
            "id": request_id,
        }
        if self.log_http_requests:
            _LOGGER.debug("[HTTP_REQUEST] %s: %s", url, body)

        # send the request to the API endpoint
        try:
            response = await self._websession.request("POST", url, json=body, timeout=self._timeout)
        except Exception as exception:
            raise ConnectionFailed(f"{exception}") from exception

        # parse the response and look for errors
        response_status = response.status
        if self.log_http_requests:
            _LOGGER.debug("[HTTP_RESPONSE] %s: %s", response_status, await response.text())
        if response_status != 200:
            raise APIError(f"status code {response.status}")
        try:
            response_body = await response.json(content_type="text/plain")
        except Exception as exception:
            raise InvalidResponse(f"unable to parse response text {await response.text()}") from exception
        if (
            "result" not in response_body
            or "code" not in response_body["result"]
            or "msg" not in response_body["result"]
        ):
            raise InvalidResponse(f"cannot find result, code or msg in {response_body}")
        result_code = response_body["result"]["code"]
        result_message = response_body["result"]["msg"]
        if result_code != "0":
            error_message = result_code + ": " + result_message
            if result_code in ("OP1008", "SN1001"):
                raise InvalidConfiguration(f"Invalid appId or appSecret ({error_message})")
            if result_code == "OP1009":
                raise NotAuthorized(f"{error_message}")
            raise APIError(error_message)

        # return the payload of the reponse
        response_data = response_body["result"]["data"] if "data" in response_body["result"] else {}
        return response_data

    async def async_api_deviceBaseList(self) -> dict:  # pylint: disable=invalid-name
        """Return the list of registered devices \
            (https://open.imoulife.com/book/http/device/manage/query/deviceBaseList.html)."""
        # define the api endpoint
        api = "deviceBaseList"
        # preparare the payload
        payload = {
            "bindId": -1,
            "limit": 20,
            "type": "bindAndShare",
            "needApInfo": False,
        }
        # call the api
        return await self._async_call_api(api, payload)

    async def async_api_deviceBaseDetailList(self, devices: list[str]) -> dict:  # pylint: disable=invalid-name
        """Return the details of the requested devices \
            (https://open.imoulife.com/book/http/device/manage/query/deviceBaseDetailList.html)."""
        # define the api endpoint
        api = "deviceBaseDetailList"
        # preparare the payload
        device_list = []
        for device in devices:
            device_list.append({"deviceId": device, "channelList": "0"})
        payload = {"deviceList": device_list}
        # call the api
        return await self._async_call_api(api, payload)

    async def async_api_deviceOnline(self, device_id: str) -> dict:  # pylint: disable=invalid-name
        """Device online or offline \
            (https://open.imoulife.com/book/http/device/manage/query/deviceOnline.html)."""
        # define the api endpoint
        api = "deviceOnline"
        # preparare the payload
        payload = {"deviceId": device_id}
        # call the api
        return await self._async_call_api(api, payload)

    async def async_api_getDeviceCameraStatus(  # pylint: disable=invalid-name
        self, device_id: str, enable_type: str
    ) -> dict:
        """Get the status of the device switch \
            (https://open.imoulife.com/book/http/device/config/ability/getDeviceCameraStatus.html)."""
        # define the api endpoint
        api = "getDeviceCameraStatus"
        # preparare the payload
        payload = {
            "deviceId": device_id,
            "enableType": enable_type,
        }
        # call the api
        return await self._async_call_api(api, payload)

    async def async_api_setDeviceCameraStatus(  # pylint: disable=invalid-name
        self, device_id: str, enable_type: str, value: bool
    ) -> dict:
        """Set a device switch \
            (https://open.imoulife.com/book/http/device/config/ability/setDeviceCameraStatus.html)."""
        # define the api endpoint
        api = "setDeviceCameraStatus"
        # preparare the payload
        payload = {"deviceId": device_id, "enableType": enable_type, "enable": value}
        # call the api
        return await self._async_call_api(api, payload)

    async def async_api_getAlarmMessage(self, device_id: str) -> dict:  # pylint: disable=invalid-name
        """Get the device message list of the device channel in the specified time period \
            (https://open.imoulife.com/book/http/device/alarm/getAlarmMessage.html)."""
        # define the api endpoint
        api = "getAlarmMessage"
        # preparare the payload
        end_time = datetime.now()
        begin_time = end_time - timedelta(days=30)
        payload = {
            "deviceId": device_id,
            "count": "1",
            "channelId": "0",
            "beginTime": begin_time.strftime("%Y-%m-%d %H:%M:%S"),
            "endTime": end_time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        # call the api
        return await self._async_call_api(api, payload)
