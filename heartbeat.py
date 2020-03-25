import ConnectLocal
from requests import get
from requests.auth import HTTPBasicAuth as auth

creds = auth("guest","guest")
url = "http://localhost:15672/api/aliveness-test/%2F"

#aliveness
def check_alive():
    response = get(url, creds)
    status = response.json()
    print("aliveness test returned with '{0}".format(response.status_code))
    print(status)

#tcp
def connect():
    return ConnectLocal.connect_heartbeat()

while(True):
    channel = connect()

    try:
        check_alive()
        channel.basic_publish("","pika_queue",body="aliveness")
    except:
        print("not alive--action required")
    v = input ("press ctrl+c to stop or any key to continue publishing")