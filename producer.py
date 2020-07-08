# coding: utf-8
import time
from kafka import KafkaProducer

# 实例化一个KafkaProducer示例，用于向Kafka投递消息
producer = KafkaProducer(bootstrap_servers='localhost:9092')

producer.send('rawContent', "hello world".encode('utf8'))

time.sleep(1)
