from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "test-topic",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",  # 'earliest' reads old + new, 'latest' only new
    group_id="my-group"
)

print("Starting consumer...")
for message in consumer:
    print(f"Received: key={message.key}, value={message.value.decode()}")
