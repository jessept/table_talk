# table_talk
Table talk is a basic chat program that leverages Kafka's pub/sub model and rest API.

In order for it to work, Kafka's REST API needs to be installed and working, so if you don't have it installed, use [this quickstart link] (http://docs.confluent.io/3.0.0/kafka-rest/docs/intro.html#kafkarest-intro).

Once confluent is installed, make sure you have the following running

./bin/zookeeper-server-start ./etc/kafka/zookeeper.properties

./bin/kafka-server-start ./etc/kafka/server.properties

./bin/schema-registry-start ./etc/schema-registry/schema-registry.properties

./bin/kafka-rest-start ./etc/kafka-rest/kafka-rest.properties
