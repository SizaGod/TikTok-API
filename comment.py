import requests
from Gorgon import Gorgon
from Argus import Argus
from Ladon import Ladon
from urllib.parse import urlencode
from hashlib import md5
import time
def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "v04.04.05-ov-android", sdk_version: int = 134744640, platform: int = 0, unix: int = None):
        x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
        if not unix: unix = int(time.time())
    
        return Gorgon(params, unix, payload, cookie).get_value() | { 
            "x-ladon"   : Ladon.encrypt(unix, license_id, aid),
            "x-argus"   : Argus.get_sign(params, x_ss_stub, unix,
                platform        = platform,
                aid             = aid,
                license_id      = license_id,
                sec_device_id   = sec_device_id,
                sdk_version     = sdk_version_str, 
                sdk_version_int = sdk_version
            )
        }
def base_params():
        return {
  'device_id':None,
  'version_name':None,
  'os': "android",
  '_rticket': "1723510777868",
  'is_pad': "0",
  'last_install_time': "1721568224",
  'host_abi': "arm64-v8a",
  'content_language': "en,ar,",
  'ts': "1723510775",
  'is_landscape': "0"
        }
def algo():
 params = base_params()
 return sign(urlencode(params),payload)
cook="store-idc=maliva; tt-target-idc=useast1a; passport_csrf_token=8d61780311359a828c44d3fc71926d31; passport_csrf_token_default=8d61780311359a828c44d3fc71926d31; store-country-code=dz; store-country-code-src=uid; d_ticket=fa47ea5a5a736ed7832c796a869c0bf616085; multi_sids=6907270777931711494%3A7579d1112e1d3e3fc3dbd3d9663db299%7C7394234693875057670%3A0fcd357489c911526b9df0e9eac8c8d3; odin_tt=a614b5395640c6f65241bb6c30523c7dbeed1d0e6b8f37d6e3e73f11a9e796259dd3918bf452793a7889401c11110268b64b756308076723c820e456c35ca71151bca4ed756246e83c3507ee032fb947; cmpl_token=AgQQAPMvF-RPsI_lYIqWPJ0__O-Q0kgJP4ekYNWr0A; sid_guard=7579d1112e1d3e3fc3dbd3d9663db299%7C1723071654%7C15552000%7CMon%2C+03-Feb-2025+23%3A00%3A54+GMT; uid_tt=17221740f000b2678a4a6a64bc7e8320e36434a14225e2b1ec9cce58a65d68a4; uid_tt_ss=17221740f000b2678a4a6a64bc7e8320e36434a14225e2b1ec9cce58a65d68a4; sid_tt=7579d1112e1d3e3fc3dbd3d9663db299; sessionid=7579d1112e1d3e3fc3dbd3d9663db299; sessionid_ss=7579d1112e1d3e3fc3dbd3d9663db299; install_id=7389856192924976902; ttreq=1$0d2e569624f35c738d2c54bb1ac8f202c82746ab; msToken=Tht9DGSb5xZ4eSnSwE_0DzueU47kDpxO46ebb06ElrNziYCwqpkMTk9fiFJC8_P-Fo-WFs73PYRx1Hf8Z2Kh9L5Veco8vcC4c31e7FUXhj2omPIjp8exxJ_CH6bV"
iid='7389856192924976902'
did='7389854904419223045'
awid='7348952636785167621'
text='commentapi'
url = "https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/comment/publish/"
payload = f"aweme_id={awid}&text={text}&text_extra=%5B%5D&image_extra=%5B%5D&is_self_see=0&channel_id=0&action_type=0&publish_scenario=3&skip_rethink=0&current_shown_count=148"
headers = {
  'User-Agent': "com.zhiliaoapp.musically/2023503040 (Linux; U; Android 12; en; CPH2121; Build/SP1A.210812.016; Cronet/TTNetVersion:711894ae 2024-06-04 QuicVersion:5f987023 2024-05-10)",
  'x-bd-kmsv': "0",
  'x-tt-dm-status': "login=1;ct=1;rt=1",
  'x-ss-req-ticket': "1723509848275",
  'tt-ticket-guard-version': "3",
  'passport-sdk-version': "6010290",
  'x-vc-bdturing-sdk-version': "2.3.8.i18n",
  'x-tt-store-region': "dz",
  'x-tt-store-region-src': "uid",
  'x-ss-dp': "1233",
  'x-argus':algo()['x-argus'],
  'x-gorgon': algo()['x-gorgon'],
  'x-khronos':algo()['x-khronos'],
  'x-ladon':algo()['x-ladon'],
  'Cookie': cook
}
response = requests.post(url, params=urlencode(base_params()), headers=headers)
print(response.text)