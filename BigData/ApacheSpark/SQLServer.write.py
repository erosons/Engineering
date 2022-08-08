rite to a new SQL Table
== == == == == == == == == == == == ==

server_name = "jdbc:sqlserver://{SERVER_ADDR}"
database_name = "database_name"
url = server_name + ";" + "databaseName=" + database_name + ";"

table_name = "table_name"
username = "username"
password = "password123!#"  # Please specify password here

try:
    df.write \
      .format("com.microsoft.sqlserver.jdbc.spark") \
      .mode("overwrite") \
      .option("url", url) \
      .option("dbtable", table_name) \
      .option("user", username) \
      .option("password", password) \
      .save()
except ValueError as error:
    print("Connector write failed", error)
