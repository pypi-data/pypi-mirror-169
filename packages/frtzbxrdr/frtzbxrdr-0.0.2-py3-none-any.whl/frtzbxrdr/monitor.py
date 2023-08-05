import logging
import time
from typing import Callable, List
import schedule
import requests
from .auth import get_sid

__author__ = "Daniel Ewert"
__copyright__ = "Daniel Ewert"
__license__ = "MIT"

_logger = logging.getLogger(__name__)

SID_URL = "http://fritz.box"
DATA_URL = "http://fritz.box/data.lua"


def get_network_page(sid):
    params = {
        "xhr": "1",
        "sid": sid,
        "page": "netDev",
        "xhrId": "all",
        "initial": ""
    }
    resp = requests.post(DATA_URL, params)
    return resp.json()


class Monitor:

    def __init__(self, user: str, password: str) -> None:
        self._user = user
        self._password = password
        self._current_sid = None
        self._macs_scanned_last_time = []
        self._mac_gone_callback = None
        self._mac_appeared_callback = None

    def run_forever(self, refresh_rate=5):
        self._refresh_sid()
        _logger.debug("logged into fritzbox, session id: %s", self._current_sid)
        schedule.every(30).minutes.do(self._refresh_sid)
        while True:
            schedule.run_pending()
            self._update_devices()
            time.sleep(refresh_rate)

    def check_once(self):
        self._refresh_sid()
        self._update_devices()

    def _update_devices(self):
        network_data = get_network_page(self._current_sid)
        devices = network_data["data"]["active"]
        scanned_macs = [device["mac"] for device in devices]
        _logger.debug(f"Read macs: {scanned_macs}")
        if self._mac_gone_callback:
            macs_gone = [
                mac for mac in self._macs_scanned_last_time if not mac in scanned_macs]
            for mac_gone in macs_gone:
                self._mac_gone_callback(mac_gone)

        if self._mac_appeared_callback:
            new_macs = [
                mac for mac in scanned_macs if not mac in self._macs_scanned_last_time]
            for new_mac in new_macs:
                self._mac_appeared_callback(new_mac)

        self._macs_scanned_last_time = scanned_macs

    def _refresh_sid(self):
        self._current_sid = get_sid(SID_URL, self._user, self._password)

    def get_all_connected_macs(self) -> List[str]:
        return self._macs_scanned_last_time

    def on_device_connected(self, callback: Callable[[str], None]) -> None:
        _logger.debug("Registered callback for device connections")
        self._mac_appeared_callback = callback

    def on_device_disconnected(self, callback: Callable[[str], None]) -> None:
        _logger.debug("Registered callback for device disconnections")
        self._mac_gone_callback = callback
