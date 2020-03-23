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

