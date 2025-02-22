import pika

def on_message_received(ch, method, properties, body):
    print(f"Received message is {body}")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue="letterbox")

channel.basic_consume(queue="letterbox",
                      auto_ack=True,
                      on_message_callback=on_message_received)

print("Starting Consuming...")

channel.start_consuming()