from kafka import KafkaConsumer
 
consumer = KafkaConsumer('wordStats')
for msg in consumer:
    print((msg.value).decode('utf8'))
