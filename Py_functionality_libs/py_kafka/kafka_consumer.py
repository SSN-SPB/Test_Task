from kafka import KafkaConsumer, TopicPartition
import json
import datetime


def get_kafka_messages(
    server,
    topic,
    min_time,
    expected_event_type=None,
    ssl_cafile=None,
    ssl_keyfile=None,
    ssl_certfile=None,
):
    test_consumer = KafkaConsumer(
        api_version=(0, 10, 1),
        security_protocol="SSL",
        bootstrap_servers=[server],
        client_id="test",
        group_id="test",
        ssl_cafile=ssl_cafile,
        ssl_keyfile=ssl_keyfile,
        ssl_certfile=ssl_certfile,
        auto_offset_reset="earliest",
    )
    message_list = []
    tp = TopicPartition(topic, 1)
    test_consumer.assign([tp])
    count = test_consumer.position(tp)
    print("Number of messages: {}".format(count))

    test_consumer.poll()
    test_consumer.seek_to_beginning(tp)
    minimal_message_time = set_datetime_object(min_time)
    print("Left bound of the time interval: {}".format(minimal_message_time))

    for message in test_consumer:
        try:
            message_timestamp = set_datetime_object(
                json.loads(message.value)["timestamp"]
            )
        except (ValueError, KeyError):
            print(
                "Oops!  That was no valid 'timestamp' key in message: {}".format(
                    message.value
                )
            )
            continue
        if message_timestamp > minimal_message_time:
            message_list.append(message.value)
            print("Message {} added to message list".format(message.value))
        if (
            len(message_list) > 0
            and test_consumer.position(tp) >= count
            and check_expected_event_type(expected_event_type, message)
        ):
            return message_list
    test_consumer.close()


def check_expected_event_type(expected_event_type, message):
    if (
        expected_event_type is not None
        and json.loads(message.value)["eventType"] == expected_event_type
    ) or expected_event_type is None:
        return True
    else:
        return False


def set_datetime_object(time):
    if "." in time:
        return datetime.datetime.strptime(time.replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
    else:
        return datetime.datetime.strptime(time.replace("Z", ""), "%Y-%m-%dT%H:%M:%S")
