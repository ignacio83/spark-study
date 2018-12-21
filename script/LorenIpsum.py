from pyspark.sql import SparkSession
from pyspark.sql.functions import *

textFile = "/Users/andre.ignacio/Documents/workspacePy/spark-study/data/loren_ipsum.txt"
spark = SparkSession.builder.appName("LorenIpsun").getOrCreate()
fileData = spark.read.text(textFile).cache()

wordCounts = fileData.select(explode(split(fileData.value, '\s+')).alias("word")).groupBy("word").count()

result = wordCounts.collect()

print (result)

spark.stop()
