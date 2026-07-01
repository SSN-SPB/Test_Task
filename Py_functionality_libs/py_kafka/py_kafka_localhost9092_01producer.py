# run kafka server locally before running this code
# To run kafka server locally, follow these steps:
# 1. Download and install Apache Kafka from the official website: https://kafka.apache
# 2. Start the Zookeeper server by running the following command in the terminal:
#    bin/zookeeper-server-start.sh config/zookeeper.properties
# 3. Start the Kafka server by running the following command in the terminal:
#    bin/kafka-server-start.sh config/server.properties
# 4. Create a topic named "test-topic" by running the following command in the terminal:
#    bin/kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092

# or by docker: "docker run -d --name kafka -p 9092:9092 apache/kafka"

# install kafka-python library before running this code: pip install kafka-python
# check it by running: pip show kafka-python
# Name: kafka-python
# Version: 2.3.0
# Run command: python .\py_kafka_localhost9092_02consumer.py
# in the separate terminal, run command: python .\py_kafka_localhost9092_01producer.py
# Expect output in producer terminal:
# Sent: {'user_id': 1, 'action': 'login'}
# Sent: {'user_id': 2, 'action': 'buy'}
# Sent: {'user_id': 3, 'action': 'logout'}
# Sent: {'user_id': 4, 'action': 'login'}
# All messages sent
# Expect output in consumer terminal:
# Listening for target message...
# Received: {'user_id': 1, 'action': 'login'}
# Received: {'user_id': 2, 'action': 'buy'}
# Received: {'user_id': 3, 'action': 'logout'}
# 🎯 FOUND TARGET MESSAGE: {'user_id': 3, 'action': 'logout

from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

messages = [
    {"user_id": 1, "action": "login"},
    {"user_id": 2, "action": "buy"},
    {"user_id": 3, "action": "logout"},
    {"user_id": 4, "action": "login"},
]

for msg in messages:
    producer.send("test-topic", value=msg)
    print(f"Sent: {msg}")
    time.sleep(0.5)

producer.flush()
print("All messages sent")
