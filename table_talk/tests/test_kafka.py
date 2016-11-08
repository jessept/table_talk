from table_talk.kafka_client import KafkaClient
from io import StringIO


class TestKafkaClient:
    def setUp(self):
        self.topic = 'test1'
        self.host = 'http://localhost:8082'
        self.name = 'test2'
        self.message = 'message1'
        self.client = KafkaClient(topic=self.topic, host=self.host, name=self.name)
        self.topic_list = self.client.get_current_topics()
        self.client.create_topic()
        self.out = StringIO()
        self.response = self.client.post_to_topic(self.message)



    def tearDown(self):
        self.client = ''

    def test_KafkaClient_attributes(self):
        assert self.client._host == self.host
        assert self.client._headers == {'Content-Type': 'application/vnd.kafka.json.v1+json',}
        assert self.client._name == self.name
        assert self.client._topic == self.topic
        assert self.client._new is False

    def test_current_topics(self):
        assert 'test1' in self.topic_list
        assert 'crazy_test_aksjhfkjasd' not in self.topic_list

    def test_post_message(self):
        assert self.response.status_code == 200

    #def test_read_message(self):
        #self.client.read_from_topic(out=self.out, max_messages=1)
        #output = self.out.getvalue().strip('\n').split(':')[-1].strip()
        #assert output == 'message1'
