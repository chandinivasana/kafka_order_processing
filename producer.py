import json
import uuid
import time
import random
from confluent_kafka import Producer

producer_config = {"bootstrap.servers": "localhost:9092"}
producer = Producer(producer_config)

def delivery_report(err, msg):
    if err:
        print(f"Delivery failed: {err}")
    else:
        print(f"Delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

def generate_order():
    users = ["chan", "nana", "john", "doe", "alice"]
    items = ["pinky pasta", "blue burger", "green salad", "yellow yogurt", "red rice"]
    
    return {
        "order_id": str(uuid.uuid4()),
        "user": random.choice(users),
        "item": random.choice(items),
        "quantity": random.randint(1, 10),
        "timestamp": time.time()
    }

def main():
    print("Starting producer...")
    try:
        while True:
            order = generate_order()
            value = json.dumps(order).encode("utf-8")
            
            producer.produce(
                topic="orders",
                value=value,
                key=order["order_id"],
                callback=delivery_report
            )
            producer.poll(0)
            print(f"Produced order: {order['order_id']}")
            time.sleep(2)  # Produce an order every 2 seconds
    except KeyboardInterrupt:
        print("Stopping producer...")
    finally:
        producer.flush()

if __name__ == "__main__":
    main()
