from kafka import KafkaConsumer
import getpass
import requests
import json
import sys


# 6.) Testing

class KafkaClient:
    def __init__(self, topic='', host='http://localhost:8082', name=getpass.getuser()):
        self._host = host
        self._headers = {'Content-Type': 'application/vnd.kafka.json.v1+json',}
        self._headers_accept = {'Accept': 'application/vnd.kafka.json.v1+json',}
        self._name = name
        self._topic = self.get_topic(topic)
        self._new = self.check_new()
        self._consumer = self.subscribe_to_topic()

    def get_topic(self, init_topic):
        if init_topic == '':
            return 'user-{}'.format(self._name)
        else:
            return init_topic

    def get_current_topics(self):
        host = self._host
        try:
            r = requests.get(host + '/topics')
        except ConnectionRefusedError:
            raise ConnectionRefusedError('Connection to Kafka REST API refused, please ensure it is running correctly')
        topic_list = []
        for topic in r.json():
            if topic[0] == '_':
                pass
            else:
                topic_list.append(topic)
        return topic_list

    def check_new(self):
        topic_check = self._topic
        topic_list = self.get_current_topics()
        return topic_check not in topic_list

    def subscribe_to_topic(self):
        topic = self._topic
        consumer = KafkaConsumer(topic)
        return consumer

    def create_topic(self):
        #data_dict = {"records": [{"value": {'user': self._name, 'message': 'Starting Channel {}'.format(self._topic)}}]}
        #msg = json.dumps(data_dict)
        data = '{"name": "my_consumer_instance", "format": "json", "auto.offset.reset": "smallest"}'
        resp = requests.post('{0}/consumers/my_json_consumer'.format(self._host), headers=self._headers, data=data)
        #api_response = requests.post('{0}/topics/{1}'.format(self._host, self._topic), headers=self._headers, data=msg)
        return resp

    def read_from_topic(self, out=sys.stdout, max_messages=1e10):
        if self._new:
            self.create_topic()
        # consumer = self._consumer
        name = self._name
        while max_messages:
            f = requests.get(
                '{0}/consumers/my_json_consumer/instances/my_consumer_instance/topics/{1}'.format(self._host,
                                                                                                  self._topic),
                headers=self._headers_accept)
            for message in f.json():
                user = message['value']['user']
                chat = message['value']['message']
                if user == name:
                    pass
                else:
                    out.write(('\n{0}: {1}\n'.format(user, chat)))
                    out.flush()
            max_messages -= 1

    def post_to_topic(self, message):
        user = self._name
        msg_dict = {"records": [{"value": {'user': user, 'message': message}}]}
        msg = json.dumps(msg_dict)
        response = requests.post('{0}/topics/{1}'.format(self._host, self._topic), headers=self._headers, data=msg)
        return response
