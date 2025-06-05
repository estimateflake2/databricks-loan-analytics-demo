# Databricks notebook source
# MAGIC %run "/Finance Services/Sample Finance Notebook"
# MAGIC

# COMMAND ----------

db_ApplicationDataSet.write.format('delta').mode('overwrite').option('path','abfss://destination@estimateflake.dfs.core.windows.net/newFolder/newData.csv').save()

# COMMAND ----------

client_id = dbutils.secrets.get(scope = "josephScope", key = "clientId")
client_secret = dbutils.secrets.get(scope = "josephScope", key = "clientSecret")
tenant_id = dbutils.secrets.get(scope = "josephScope", key = "tenantId")

spark.conf.set("fs.azure.account.auth.type.estimateflake.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.estimateflake.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.estimateflake.dfs.core.windows.net", client_id)
spark.conf.set("fs.azure.account.oauth2.client.secret.estimateflake.dfs.core.windows.net", client_secret)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.estimateflake.dfs.core.windows.net", "https://login.microsoftonline.com/6bfc8671-619b-4ced-b994-3487bacee61d/oauth2/token")
print ("works")

# -- getting data from Storage Account --
db_ApplicationDataSet = spark.read.format("csv")\
                .option("header", "true")\
                .option("inferSchema", "true").load("abfss://source@estimateflake.dfs.core.windows.net/Loan_Application_Dataset.csv")
db_CustomerTable = spark.read.format("csv")\
                .option("header", "true")\
                .option("inferSchema", "true").load("abfss://source@estimateflake.dfs.core.windows.net/Customer_Table.csv")      
db_Loan_Table = spark.read.format("csv")\
                .option("header", "true")\
                .option("inferSchema", "true").load("abfss://source@estimateflake.dfs.core.windows.net/Loan_Table.csv")   
#--------------------------------------------------------                

db_ApplicationDataSet.createOrReplaceTempView("loan_applications");
db_CustomerTable.createOrReplaceTempView("customers");
db_Loan_Table.createOrReplaceTempView("loans");

spark.sql("""
select 
    a.loan_id, 
    c.loan_name,
    b.customer_id, 
    b.first_name, 
    b.last_name,
    c.loan_purpose,
    c.application_date,
    c.creation_date
from loan_applications a
left join customers b on a.customer_id = b.customer_id
left join loans c on a.loan_id = c.loan_id 
order by b.first_name, b.last_name, c.application_date desc
""")

