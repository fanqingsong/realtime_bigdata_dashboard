

./bin/start_kafka.sh &

sleep 10s

./bin/start_word_counter.sh &

sleep 5s

./bin/start_flask.sh &




