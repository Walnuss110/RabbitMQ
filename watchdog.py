import pika
import requests
from requests.auth import HTTPBasicAuth
import time

_status="backing_queue_status"
_arguments=