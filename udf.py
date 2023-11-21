# Databricks notebook source
udfExampleDF = spark.range(5).toDF("sal")


# COMMAND ----------

udfExampleDF.show()

# COMMAND ----------

def power3(double_value):
    return double_value ** 3

# COMMAND ----------

power3(2.0)

# COMMAND ----------

from pyspark.sql.functions import *

power3udf= udf(power3)

# udfExampleDF.select(power3("sal")).show()

# COMMAND ----------

udfExampleDF.select(power3udf(col("sal")),col("sal")).show()
