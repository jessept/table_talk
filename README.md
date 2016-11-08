# What is table_talk?
Table talk is a basic chat program that leverages Kafka's pub/sub model and rest API.

In order for it to work, Kafka's REST API needs to be installed and working, so if you don't have it installed, use [this quickstart link] (http://docs.confluent.io/3.0.0/kafka-rest/docs/intro.html#kafkarest-intro).

# After Kafka's REST API is installed, make sure the following are running:

./bin/zookeeper-server-start ./etc/kafka/zookeeper.properties

./bin/kafka-server-start ./etc/kafka/server.properties

./bin/schema-registry-start ./etc/schema-registry/schema-registry.properties

./bin/kafka-rest-start ./etc/kafka-rest/kafka-rest.properties

# Installing table_talk

Simply run "pip install git+git://github.com/jessept/table_talk.git" 

# Examples

table_talk -t test_channel
Successfully opened channel test_channel

