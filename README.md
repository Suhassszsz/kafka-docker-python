🚀 Kafka + Python Example

This project demonstrates how to run a Kafka cluster locally using Docker Compose and interact with it using a Python producer and consumer.

📂 Project Structure
- kafka-docker-python/

│── docker-compose.yml  

│── producer.py        

│── consumer.py    

│── requirements.txt  

│── README.md            




🐳 1. Start Kafka Cluster
docker-compose up -d


Verify containers are running:

docker ps


You should see zookeeper and broker.




📌 2. Create a Kafka Topic
docker exec -it broker kafka-topics \
  --create --topic test-topic \
  --bootstrap-server broker:9092 \
  --partitions 1 --replication-factor 1


List topics:

docker exec -it broker kafka-topics --list --bootstrap-server broker:9092



💻 3. Install Python Dependencies

pip install -r requirements.txt



📨 4. Run Producer

python3 producer.py

This will send 10 messages (Hello Kafka 0 … Hello Kafka 9) to the topic.



📥 5. Run Consumer

python3 consumer.py

Behavior depends on auto_offset_reset:

"earliest" → reads all old + new messages.

"latest" → only reads new messages produced after consumer starts.



🔧 6. Kafka CLI Commands
Produce from CLI
docker exec -it broker kafka-console-producer \
  --topic test-topic --bootstrap-server broker:29092

Consume from CLI
docker exec -it broker kafka-console-consumer \
  --topic test-topic --from-beginning --bootstrap-server broker:29092

Check Consumer Groups
docker exec -it broker kafka-consumer-groups \
  --bootstrap-server broker:29092 --list





