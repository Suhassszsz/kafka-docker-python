
from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers="localhost:9092")

for i in range(10):
    key = str(i).encode("utf-8")
    value = f"Hello Kafka {i}".encode("utf-8")
    producer.send("test-topic", key=key, value=value)
    print(f"Sent: {value.decode()}")
    time.sleep(1)

producer.flush()
producer.close()
