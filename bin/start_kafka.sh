
# run zookeeper
cd /usr/local/kafka
bin/zookeeper-server-start.sh config/zookeeper.properties &
cd -


# run kafka
rm -rf /tmp/kafka-logs/*
cd /usr/local/kafka
bin/kafka-server-start.sh config/server.properties
cd -





