## sbt project compiled with Scala 3

### Usage

This is a normal sbt project. You can compile code with `sbt compile`, run it with `sbt run`, and `sbt console` will start a Scala 3 REPL.

For more information on the sbt-dotty plugin, see the
[scala3-example-project](https://github.com/scala/scala3-example-project/blob/main/README.md).

<!-- kafka procedure -->

<!-- start zookeeper -->
bin/zookeeper-server-start.sh config/zookeeper.properties

<!-- start kafka -->
bin/kafka-server-start.sh config/server.properties

<!-- create -->
bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic fakedata
<!-- delete -->
bin/kafka-topics.sh --delete --bootstrap-server localhost:9092 --topic fakedata