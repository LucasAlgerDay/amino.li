__title__ = 'Amino.li'
__author__ = 'Lucas'
__license__ = 'MIT'
__copyright__ = 'Copyright 2023'
__version__ = '0.3'

from .acm import ACM
from .client import Client
from .sub_client import SubClient
from .lib.util import exceptions, helpers, objects, headers
from .asyncfix import acm, client, sub_client, socket
from .socket import Callbacks, SocketHandler
from requests import get
from json import loads
