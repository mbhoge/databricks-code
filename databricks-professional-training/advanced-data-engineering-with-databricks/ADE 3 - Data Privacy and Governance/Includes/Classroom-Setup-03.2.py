# Databricks notebook source
# MAGIC %run ./Classroom-Setup-03-Common

# COMMAND ----------

notebooks = [
    "ADE 3.1.1 - PII Lookup Table",
    "ADE 3.1.2 - Pseudonymized ETL"
]
DA.configure_pipeline(configuration={"source": DA.paths.stream_source, "lookup_db": DA.lookup_db}, notebooks=notebooks)
DA.user_reg_stream.load(continuous=True)
DA.daily_stream.load()
DA.conclude_setup()

None


