import pika
import ConnectLocal

credentials = pika.PlainCredentials("guest", "guest")
conn_param = pika.ConnectionParameters(credentials=credentials)

_connection = pika.BlockingConnection(parameters=conn_param)

def client(corr_id, msg):
    print("start client with {0} and {1}".format(corr_id,msg))

    ch=_connection.channel()

    response_queue="response_queue"
    
