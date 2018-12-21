#Start Spark Cluster

./sbin/start-master.sh --webui-port 9090
./sbin/start-slave.sh spark://<localmachine>:7077 --cores 2 --memory=2g

#Running a script

```export SPARK_HOME=<YOUR_SPARK_HOME>```
```export SPARK_MASTER=<YOUR_SPARK_MASTER>```
Run a shell script of your app, all bashs is in bash folder.

