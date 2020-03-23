import pika
import sys
import ConnectLocal


bind_simple = True
if len(sys.argv) > 1:
    bind_simple = False

    #connect
channel = ConnectLocal.do_connect()
if bind_simple:
    channel.queue_declare("simple_bind")
    print("implicit binding is done-->check the management UI")
else:
    channel.queue_declare("direct_bind")
    channel.queue_bind(queue="direct_bind", exchange="amq.direct", routing_key="demonstrate")
    print("direct binding with routing_key demonstrate")

# close connection

channel.close()

