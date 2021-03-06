from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable

import json
import time
import sys

KAFKA_HOST = sys.argv[1]+':9094'
print('kafka host: ' + KAFKA_HOST)
try:
    producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        bootstrap_servers=KAFKA_HOST)
except NoBrokersAvailable:
    sys.exit('broker not available (yet?)')

if not producer.bootstrap_connected():
    sys.exit('not connected, restarting...')

try:
    print('producing')
    while True:
        producer.send('test-local', value={"hello": "local-producer"})
        # wait for send IMPORTANT IF NOT IN WHILE LOOP!
        producer.flush()
        time.sleep(1)
        print('produced one message')
except Exception as e:
    print(repr(e))
    producer.flush()
    producer.close()
    


