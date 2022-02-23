import click
import pika


@click.command()
@click.option(
    "--host",
    type=str,
    required=True
)
@click.option(
    "--topic",
    type=str,
    required=True
)
@click.option(
    "--message",
    type=str,
    required=True
)
def publish(host, topic, message):
    pika_param = pika.ConnectionParameters(host)
    properties = pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)

    with pika.BlockingConnection(pika_param) as connection:
        channel = connection.channel()
        channel.queue_declare(queue=topic, durable=True)

        channel.basic_publish(exchange="", routing_key=topic, body=message, properties=properties)


if __name__ == "__main__":
    
    publish()
