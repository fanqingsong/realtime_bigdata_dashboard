# coding: utf-8
import csv
import time
from kafka import KafkaProducer

# 实例化一个KafkaProducer示例，用于向Kafka投递消息
producer = KafkaProducer(bootstrap_servers='localhost:9092')

for i in range(10):
    time.sleep(1) 
    # 发送数据，topic为'sex'
    producer.send('rawContent', "hello world".encode('utf8'))
