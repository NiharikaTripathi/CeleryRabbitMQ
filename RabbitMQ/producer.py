import pika

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue="letterbox")

message = "Hello!! This is my message. Mucho gusto!!"

channel.basic_publish(exchange="", routing_key="letterbox", body=message)

print(f"Sent message is {message}")

connection.close()
