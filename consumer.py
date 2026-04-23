import json
from confluent_kafka import Consumer, KafkaError

consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "order-processor-group",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(consumer_config)
consumer.subscribe(["orders"])

def main():
    print("Starting consumer...")
    try:
        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f"Consumer error: {msg.error()}")
                    break

            order = json.loads(msg.value().decode("utf-8"))
            print(f"Processed order: {order['order_id']} for {order['user']} - {order['quantity']}x {order['item']}")
            
    except KeyboardInterrupt:
        print("Stopping consumer...")
    finally:
        consumer.close()

if __name__ == "__main__":
    main()
