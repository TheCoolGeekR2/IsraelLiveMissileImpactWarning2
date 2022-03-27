from flask import Flask, render_template, Response
from pykafka import KafkaClient
from datetime import datetime
import json


def get_kafka_client():
    return KafkaClient(hosts='localhost:9092')


app = Flask(__name__)
@app.route('/')
def index():
    return(render_template('index.html'))

@app.route('/topic/<topicname>')
def get_msgs(topicname):
    client = get_kafka_client()
    def events():
        for i in client.topics[topicname].get_simple_consumer():
            if not(json.loads(i.value.decode('ascii'))["epoch"]+5 < datetime.now().timestamp()):
                yield 'data:{0}\n\n'.format(i.value.decode())
    return Response(events(), mimetype="text/event-stream")


if __name__ == '__main__':
    app.run(debug=True, port=5001)

