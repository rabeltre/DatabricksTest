# Databricks notebook source
# MAGIC %run "/Users/rbeltrecastro@outlook.com/data-engineering-with-databricks/DE 1 - Databricks Workspace/Notebook_B"

# COMMAND ----------

dbutils.widgets.text("Texto", "Marai" )

# COMMAND ----------

name = "John"
print(f"Hello {name}")
print(f"Welcome back {full_name}")
