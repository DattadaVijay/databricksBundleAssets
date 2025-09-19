# COMMAND ----------
import dlt
# COMMAND ----------
catalog_name = spark.conf.get('dltparam.catalog_name')
schema_name = spark.conf.get('dltparam.schema_name')
bundle_source = spark.conf.get('bundle.sourcePath')
# COMMAND ----------
@dlt.table

@dlt.expect("customer_id_check", "customer_id is not null")
def streaming_customers():
    df = spark.readStream.table(f"{catalog_name}.{schema_name}.customers")
    return df
# COMMAND ----------
@dlt.table

def streaming_orders():
    df = df = spark.readStream.table(f"{catalog_name}.{schema_name}.orders")
    return df

