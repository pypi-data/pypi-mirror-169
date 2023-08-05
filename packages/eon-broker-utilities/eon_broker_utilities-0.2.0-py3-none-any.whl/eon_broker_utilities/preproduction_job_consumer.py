import json
import pika
import pika.exceptions
import time
import os
import logging
import configparser




logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.getLogger("pika").setLevel(logging.ERROR)

class consumer_class(): 


    def __init__(self, service_name, handler, config):
        self.rabbit_user = config['RABBIT_USER']
        self.rabbit_password = config['RABBIT_PASSWORD']
        self.rabbit_host = config['RABBIT_HOST'] 
        self.rabbit_port = config['RABBIT_PORT']     
        self.exchange_name = config['EXCHANGE_NAME']
        self.qeue_name = service_name + '_jobs'
        self.new_jobs_routing_key = config['NEW_JOBS_ROUTING_KEY']  + service_name
        self.successful_job_routing_key = service_name + config['SUCCESSFUL_JOB_ROUTING_KEY']
        self.failed_job_routing_key = service_name + config['FAILED_JOB_ROUTING_KEY']
        self.handler = handler
        self._conn = None
        self._channel = None
        self.connect()
        self.start_consume()
    
    def connect(self):
        try:
            credentials = pika.PlainCredentials(self.rabbit_user, self.rabbit_password)

            parameters = pika.ConnectionParameters(self.rabbit_host,
                                    int(self.rabbit_port),
                                    '/',
                                    credentials)
            self._conn = pika.BlockingConnection(parameters)
            self._channel = self._conn.channel()
            print('connected to Arnoob')

        except (pika.exceptions.ConnectionBlockedTimeout, pika.exceptions.ConnectionClosed, pika.exceptions.AMQPConnectionError, Exception) as e:
            print("trying to reconnect", e)
            time.sleep(10)
            self.connect()
            
    def handle_new_message(self, channel, method, properties, body):
        try:
            message = json.loads(body)
        except Exception as err:
            channel.basic_ack(delivery_tag=method.delivery_tag)                
            return

        try:
            # self.handler(str(message))
            print("publishing at : ", self.successful_job_routing_key)
            channel.basic_publish(exchange=self.exchange_name, routing_key=self.successful_job_routing_key, body=json.dumps(message))
        except Exception as err:
            print('Error processing job', err)
            print(message)
            message['reason'] = str(err)
            channel.basic_publish(exchange=self.exchange_name, routing_key=self.failed_job_routing_key, body=json.dumps(message))
            
        channel.basic_ack(delivery_tag=method.delivery_tag)

    def start_consume(self):
        self._channel.queue_bind(exchange=self.exchange_name, queue=self.qeue_name, routing_key=self.new_jobs_routing_key)
        self._channel.basic_consume(self.qeue_name, self.handle_new_message)
        self._channel.start_consuming()


