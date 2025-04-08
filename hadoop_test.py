from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("HadoopTest").getOrCreate()

df = spark.createDataFrame([(1, "Apple"), (2, "Banana")], ["ID", "Fruit"])
df.show()