# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE student (id INT, name STRING, age INT) TBLPROPERTIES (delta.enableChangeDataFeed = true);

# COMMAND ----------

# MAGIC %sql
# MAGIC --insert into student values(2,'sridar',100)
# MAGIC
# MAGIC update student set age = 25 where id =2;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY student

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from table_changes('student', 2) where _change_type in ('insert','update_postimage')
