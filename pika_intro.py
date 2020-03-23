import pika

credentials = pika.PlainCredentials("guest", "guest")
conn_param = pika.ConnectionParameters(credentials=credentials)

#tcp connection
connection = pika.BlockingConnection(conn_param)

#get channel to get access to all methods in library
channel = connection.channel()

# use queue
queue_name = "pika_queue"

#callback-->this is how pika library works
def consume_msg(channel, method, props, body):
    print(body)
    #default methods we need to use to connect and to talk with RabbitMQ server
    channel.basic_ack(method.delivery_tag)

# basic consume where we put in the queueName and callback simply
#-->general scheme: connect-createAChannel-consume-or-publish
channel.basic_consume(queue_name,consume_msg)

#start consuming
channel.start_consuming()

