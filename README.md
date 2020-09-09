# Realtime-BigData-Dashboard

---
## Introduction
A demo for realtime dashboard, based on bigdata technology and popular realtime comunication web technology.

---
## Architect

### realtime stream
- scrawler.py ---> kafka
- kafka ---> wordCounter.py
- wordCounter.py ---> kafka
- kafka ---> app.py
- app.py ---> browser

### diagram

Note: powered by asciiflow website [asciiflow](http://asciiflow.com/)

```
+--------------+                    +------------------+                     +----------------+
|              |         1          |                  |         4           |                |
|    Scrawler  +------------------> |     Kafka        +-------------------> |       Flask    |
|              |                    |                  |                     |                |
|              |                    |                  |                     |                |
+--------------+                    +----+---------+---+                     +--------+-------+
                                         |         ^                                  |
                                         |         |                                  |
                                       2 |         |3                                 |5
                                         |         |                                  |
                                         |         |                                  |
                                         |         |                                  v
                                     +---v---------+----+                    +--------+---------+
                                     |                  |                    |                  |
                                     |      Spark Stream|                    |       Browser    |
                                     |                  |                    |                  |
                                     |                  |                    |                  |
                                     +------------------+                    +------------------+

```

### Demo

![demo](wordCloud.png)

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

- pyenv install
[reference](https://github.com/pyenv/pyenv#installation)

- install all other dependencies

```
./bin/install_deps.sh
```

- install Kafka

[reference](http://dblab.xmu.edu.cn/blog/1096-2/)

- install Spark(2.1.0)

[reference](http://dblab.xmu.edu.cn/blog/1307-2/)

---
## Run APP
### run kafka
open a new terminal, 
run such commands:

```
./bin/start_kafka.sh
```

### run wordCounter
open a new terminal, 
enter project root directory,
run such commands:

```
./bin/start_word_counter.sh
```

### run flask server

open a new terminal, 
enter project root directory,
run such commands:

```
./bin/start_flask.sh
```

Then go to browser and access url 
http://127.0.0.1:5000/#/


### run scrawler to get new page content and insert to wordCounter
open a new terminal, 
enter project root directory,
run such commands:

```
./bin/start_scrawler.sh
```

Then go to browser to see new word cloud.


## build front code if web code chaged

open a new terminal, 
enter project root directory,
run such commands:

```
./bin/build_ui.sh
```



---
## Note:
### inspiration
This project is inspired by chinese bigdata course:
http://dblab.xmu.edu.cn/post/8274/

### Markdown cheatsheet
ReadMe is written by Markdown, here is syntax cheatsheet [Markdown Syntax](https://www.markdown.xyz/cheat-sheet/)

---
## Reference
- [Spark](http://spark.apache.org/docs/2.1.0/)
- [Kafka](http://kafka.apache.org/)
- [kafka-python](https://pypi.org/project/kafka-python/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/)
- [requests](https://2.python-requests.org/en/master/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [stop-words](https://pypi.org/project/stop-words/)
- [Socket.IO](https://socket.io/)
- [vue](https://vuejs.org/v2/guide/)
- [vue-wordcloud component](https://github.com/feifang/vue-wordcloud)
