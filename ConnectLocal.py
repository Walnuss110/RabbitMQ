import pika

def do_connect():
    credentials = pika.PlainCredentials("guest", "guest")
    conn_param = pika.ConnectionParameters(credentials=credentials)

    # tcp connection
    connection = pika.BlockingConnection(conn_param)

    # get channel to get access to all methods in library
    channel = connection.channel()
    return channel
#wohoo



def connect_heartbeat():
    credentials=pika.PlainCredentials("guest","guest")
    conn_param = pika.connection.ConnectionParameters(heartbeat=1500, credentials=credentials)
    connection = pika.BlockingConnection (conn_param)

    # get channel to get access to all methods in library
    channel = connection.channel ()
    return channel

