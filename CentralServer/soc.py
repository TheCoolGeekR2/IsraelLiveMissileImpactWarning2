from pykafka import KafkaClient
import json
from datetime import datetime
import uuid


client = KafkaClient(hosts='localhost:9092')
topic = client.topics['rocket']
producer = topic.get_sync_producer()
markers = []


def generate_uuid():
    return uuid.uuid4()

def send(data):
    msg = json.dumps(data)
    producer.produce(msg.encode('ascii'))

def MapIt(m):
    data = {
        "latitude" : m[0],
        "longitude" : m[1],
        "Name" : m[2],
        "key" : str(generate_uuid()),
        "timestamp" : str(datetime.now()),
        "type" : 'ADD',
        "epoch" : datetime.now().timestamp()
    }
    send(data)


