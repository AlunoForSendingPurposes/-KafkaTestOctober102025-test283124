# Detecção de Fraude no Kafka

## Requisitos
- Apache Kafka (instalado em `localhost:9092`)
- Zookeeper (executando antes do Kafka)
- Python 3.x
- Bibliotecas Python necessárias: `kafka-python`, `sqlite3`

## Como Executar

1. Inicie o Zookeeper:
   `bash
   bin/zookeeper-server-start.sh config/zookeeper.properties`
2. Inicie o Kafka:
    `bin/kafka-server-start.sh config/server.properties`
3. Crie um tópico no Kafka:
    `bin/kafka-topics.sh --create --topic transactions --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`
4. Execute o produtor no Kafka:
    `python producer.py`
5. Execute o consumidor no Kafka:
    `python consumer.py`

