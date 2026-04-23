

This project simulates a real-time order processing system using Apache Kafka and Python.

## Components

- **Kafka Broker**: Managed via Docker Compose (KRaft mode).
- **Producer**: A Python script (`producer.py`) that generates random order events and sends them to the `orders` topic.
- **Consumer**: A Python script (`consumer.py`) that reads order events from the `orders` topic and processes them.

## Setup

1. **Start Kafka**:
   ```bash
   docker-compose up -d
   ```

2. **Install Dependencies**:
   ```bash
   pip install confluent-kafka
   ```

3. **Run Consumer**:
   ```bash
   python consumer.py
   ```

4. **Run Producer**:
   ```bash
   python producer.py
   ```

## Requirements
- Docker and Docker Compose
- Python 3.x
- `confluent-kafka` library
