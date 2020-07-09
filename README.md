# Realtime-BigData-Dashboard

---
## Introduction
a demo for realtime dashboard, based on bigdata technology and popular realtime comunication web technology.

---
## Technology
### bigdata techs:
* kafka -- tranfer all data between components
* spark streaming -- data statistics
* scrawler -- get raw data from url.


### web techs:
* flask -- python web framework
* socket.io -- frontend/backend data exchange tunnel
* vue -- popular frontend JS framework

---
## Install
### Kafka
### Spark
### Dependency

enter project root directory
run such commands:

`
./bin/install.sh
`

---
## Run
### run zookeeper
open a new terminal, 
run such commands:

```
cd /usr/local/kafka
bin/zookeeper-server-start.sh config/zookeeper.properties
```

### run kafka
open a new terminal, 
run such commands:

```
cd /usr/local/kafka
bin/zookeeper-server-start.sh config/zookeeper.properties
```

### run wordCounter
open a new terminal, 
enter project root directory,
run such commands:

```
./bin/startWordCounter.sh
```

### run wordStats Observor to watch word statistics
open a new terminal, 
enter project root directory,
run such commands:

```
python3 backend/wordStatsObserver.py
```

### run scrawler to get new page content and insert to wordCounter
open a new terminal, 
enter project root directory,
run such commands:

```
python3 backend/wordStatsObserver.py
```

