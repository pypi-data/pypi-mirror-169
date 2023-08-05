"""
Authenticate against fritzbox

Taken from https://avm.de/fileadmin/user_upload/Global/Service/Schnittstellen/AVM_Technical_Note_-_Session_ID_deutsch_Dez2020.pdf
"""
import hashlib
import logging
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
LOGIN_SID_ROUTE = "/login_sid.lua?version=2"

logger = logging.getLogger(__name__)


class LoginState:
    def __init__(self, challenge: str, blocktime: int):
        self.challenge = challenge
        self.blocktime = blocktime
        self.is_pbkdf2 = challenge.startswith("2$")


def get_sid(box_url: str, username: str, password: str) -> str:
    """ Get a sid by solving the PBKDF2 (or MD5) challenge-response
    process. 
    """
    try:
        state = get_login_state(box_url)
    except Exception as ex:
        raise Exception("failed to get challenge") from ex

    if state.is_pbkdf2:
        logger.debug("PBKDF2 supported")
        challenge_response = calculate_pbkdf2_response(
            state.challenge, password)
    else:
        logger.debug("Falling back to MD5")
        challenge_response = calculate_md5_response(state.challenge, password)
    if state.blocktime > 0:
        logger.debug("Waiting for %s seconds...", state.blocktime)
        time.sleep(state.blocktime)
    try:
        logging.debug("Sending response %s", challenge_response)
        sid = send_response(box_url, username, challenge_response)
    except Exception as ex:
        raise Exception("failed to login") from ex
    if sid == "0000000000000000":
        raise Exception("wrong username or password")
    logger.debug("Received SID: %s", sid)
    return sid


def get_login_state(box_url: str) -> LoginState:
    """ Get login state from FRITZ!Box using login_sid.lua?version=2 """
    url = box_url + LOGIN_SID_ROUTE
    http_response = urllib.request.urlopen(url)
    xml = ET.fromstring(http_response.read())
    challenge = xml.find("Challenge").text
    blocktime = int(xml.find("BlockTime").text)
    return LoginState(challenge, blocktime)


def calculate_pbkdf2_response(challenge: str, password: str) -> str:
    """ Calculate the response for a given challenge via PBKDF2 """
    challenge_parts = challenge.split("$")
    # Extract all necessary values encoded into the challenge
    iter1 = int(challenge_parts[1])
    salt1 = bytes.fromhex(challenge_parts[2])
    iter2 = int(challenge_parts[3])
    salt2 = bytes.fromhex(challenge_parts[4])
    # Hash twice, once with static salt...
    hash1 = hashlib.pbkdf2_hmac("sha256", password.encode(), salt1, iter1)
    # Once with dynamic salt.
    hash2 = hashlib.pbkdf2_hmac("sha256", hash1, salt2, iter2)
    return "{}${}".format(challenge_parts[4], hash2.hex())


def calculate_md5_response(challenge: str, password: str) -> str:
    """ Calculate the response for a challenge using legacy MD5 """
    response = challenge + "-" + password
    # the legacy response needs utf_16_le encoding
    response = response.encode("utf_16_le")
    md5_sum = hashlib.md5()
    md5_sum.update(response)
    response = challenge + "-" + md5_sum.hexdigest()
    return response


def send_response(box_url: str, username: str, challenge_response: str) -> str:
    """ Send the response and return the parsed sid. raises an Exception on
error """
    # Build response params
    post_data_dict = {"username": username, "response": challenge_response}
    post_data = urllib.parse.urlencode(post_data_dict).encode()
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    url = box_url + LOGIN_SID_ROUTE
    # Send response
    http_request = urllib.request.Request(url, post_data, headers)
    http_response = urllib.request.urlopen(http_request)
    # Parse SID from resulting XML.
    xml = ET.fromstring(http_response.read())
    return xml.find("SID").text
