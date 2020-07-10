import json
from flask import Flask, render_template
from flask_socketio import SocketIO
from kafka import KafkaConsumer
#因为第一步骤安装好了flask，所以这里可以引用
 
app = Flask(import_name=__name__,
            static_url_path='/static', # 配置静态文件的访问 url 前缀
            static_folder='./vueproj/dist/static',    # 配置静态文件的文件夹
            template_folder='./vueproj/dist/') # 配置模板文件的文件夹
            
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None
# 实例化一个consumer，接收topic为wordStats的消息
consumer = KafkaConsumer('wordStats')
 
# 一个后台线程，持续接收Kafka消息，并发送给客户端浏览器
def background_thread():
    print("-- now run back ground thread ----")
    for msg in consumer:
        wordStats = msg.value.decode('utf8')
        print(wordStats)
        socketio.emit('wordStats_msg',{'data':wordStats})
 
# 客户端发送connect事件时的处理函数
@socketio.on('test_connect')
def connect(message):
    print(message)
    global thread
    if thread is None:
        print("now start back ground task")
        # 单独开启一个线程给客户端发送数据
        thread = socketio.start_background_task(target=background_thread)
    socketio.emit('connected', {'data': 'Connected'})
 
# 通过访问http://127.0.0.1:5000/访问index.html
@app.route("/")
def handle_mes():
    return render_template("index.html")
 
# main函数
if __name__ == '__main__':
    socketio.run(app,debug=True)