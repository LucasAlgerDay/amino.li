__title__ = 'Amino.li'
__author__ = 'Lucas'
__license__ = 'MIT'
__copyright__ = 'Copyright 2023'
__version__ = '0.5'

from .acm import ACM
from .client import Client
from .sub_client import SubClient
from .lib.util import exceptions, helpers, objects, headers
from .asyncfix import acm, client, sub_client, socket
from .socket import Callbacks, SocketHandler
from requests import get
from json import loads

__newest__ = loads(get("https://pypi.org/pypi/amino.li/json").text)["info"]["version"]

if __version__ != __newest__:
    print(f"New version available: {__newest__} (Using {__version__})")
    print("Talk in discord like 「𝑴𝑶𝑵𝑺𝑻𝑬𝑹」#4545")
