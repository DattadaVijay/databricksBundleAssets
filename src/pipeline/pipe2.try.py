import dlt

@dlt.view

def joined_view():
    df_customers = spark.read.table("LIVE.streaming_customers")
    df_orders = spark.read.table("LIVE.streaming_orders")
    df = df_customers.join(df_orders, how = 'inner', on = "customer_id")
    return df

