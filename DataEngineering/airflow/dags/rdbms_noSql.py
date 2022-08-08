import airflow
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from pyspark.sql import SparkSession, functions

def processo_etl_spark():
    spark = SparkSession \
        .builder \
        .appName("Extract_from_RDBMS_Mongo") \
        .config("spark.jars.packages",
                "org.mongodb.spark:mongo-spark-connector_2.12:3.0.0,com.microsoft.sqlserver:mssql-jdbc:8.4.1.jre8") \
        .config("spark.mongodb.input.uri", "mongodb://127.0.0.1:27017/Financeiro") \
        .config("spark.mongodb.output.uri", "mongodb://127.0.0.1:27017/Financeiro") \
        .config("spark.driver.maxResultSize", "8g") \
        .config("spark.network.timeout", 10000000) \
        .config("spark.executor.heartbeatInterval", 10000000) \
        .config("spark.storage.blockManagerSlaveTimeoutMs", 10000000) \
        .config("spark.executor.memory", "10g") \
        .master("spark://192.168.0.1:7077") \
        .getOrCreate()

    starttime = datetime.now()

    # Reading Operations for a jdbc drive rdbms
    df = spark.read.format("jdbc") \
        .option("url", "jdbc:sqlserver://127.0.0.1:1433;databaseName=Teste") \
        .option("user", '****') \
        .option("password", '****') \
        .option("numPartitions", 100) \
        .option("partitionColumn", "Segment") \
        .option("lowerBound", 1) \
        .option("upperBound", 488777675) \
        .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
        .option("dbtable", "(select * from Superstore2 where Region in ('east','west') )") \
        .load()

    # aggregations opertaions
    group = df.select("OrderID","Segement","profit", "Sales") \
        .groupby(["OrderID","Segement"]).agg(functions.sum("Sales").alias("Sum_of_Sales"))
        
    # writing to a Nosql-mongo
    group.write.format("com.mongodb.spark.sql.DefaultSource") \
        .mode("overwrite") \
        .option("database", "wicked") \
        .option("collection", "superOder") \
        .save()
    Endtime = datetime.now()
    print(Endtime -  starttime)




default_args = {
    'owner': 'sam',
    'start_date': datetime(2020, 11, 18),
    'retries': 3,
	  'retry_delay': timedelta(hours=1)
}
with airflow.DAG('dag_teste_spark_documento_vencido_v01',
                  default_args=default_args,
                  schedule_interval='0 1 * * *') as dag:


    task_elt_documento_pagar = PythonOperator(
        task_id='elt_documento_pagar_spark',
        python_callable=processo_etl_spark
        dag=dag
    )

task_elt_documento_pagar 