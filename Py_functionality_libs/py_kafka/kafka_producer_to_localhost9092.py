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
# Run command: python kafka_producer_to_localhost9092.py
# Expect output: Message sent successfully

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092")
producer.send("test-topic", b"hello")
producer.flush()

print("Message sent successfully")
