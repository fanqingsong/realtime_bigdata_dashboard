

echo "----- start kafka --------"
./bin/start_kafka.sh &

sleep 15s

echo "----- start flask --------"
./bin/start_flask.sh &


sleep 15s

echo "----- start word counter --------"
./bin/start_word_counter.sh &




