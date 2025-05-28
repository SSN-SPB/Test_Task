from kafka import KafkaProducer


def add_kafka_message(
    server, topic, message, ssl_cafile=None, ssl_keyfile=None, ssl_certfile=None
):
    test_producer = KafkaProducer(
        retries=5,
        api_version=(0, 10, 1),
        client_id="test",
        acks=0,
        security_protocol="SSL",
        bootstrap_servers=[server],
        ssl_cafile=ssl_cafile,
        ssl_keyfile=ssl_keyfile,
        ssl_certfile=ssl_certfile,
    )
    print("Message: {}".format(str(message)))
    print("\nTopic: {}".format(topic))
    send_result = test_producer.send(topic, str(message))
    test_producer.close()
    print("\n{}".format(send_result.get()))
