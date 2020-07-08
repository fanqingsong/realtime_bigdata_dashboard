# 进入kafka所在的目录
cd /usr/local/kafka

rm -rf /tmp/kafka-logs/*

bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic rawContent

bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic wordStats

bin/zookeeper-server-start.sh config/zookeeper.properties&

bin/kafka-server-start.sh config/server.properties




