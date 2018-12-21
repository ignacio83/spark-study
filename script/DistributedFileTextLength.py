from pyspark.sql import SparkSession

textFile = "/Users/andre.ignacio/Documents/workspacePy/spark-study/data/loren_ipsum.txt"
spark = SparkSession.builder.appName("DistributedFileTextLength").getOrCreate()
sc = spark.sparkContext

lines = sc.textFile(textFile)
lineLengths = lines.map(lambda s: len(s))
lineLengths.cache()

listLineLengths = lineLengths.collect()

print "Lengths by line:"
for value in listLineLengths:
    print value

totalLength = lineLengths.reduce(lambda a, b: a + b)

print ("TotalLength: " + str(totalLength))
