# Loan Analytics Demo – Azure Databricks + Delta Lake

This project was built as part of my technical preparation for a Data Engineer interview. It demonstrates my hands-on work with Azure Databricks, including ingesting raw finance-related data from Azure Data Lake Storage, transforming it using PySpark, and querying it with SQL and Delta Lake.

---

## Features

- ✅ Setup and authentication using OAuth between Azure and Databricks
- ✅ Ingested CSV datasets from ADLS Gen2 into Spark DataFrames
- ✅ Created and registered temporary views in Databricks
- ✅ Wrote SQL queries to join customer, loan, and application datasets
- ✅ Saved output in Delta format
- ✅ Practiced window functions and grouped aggregations in SQL

---

## Tools & Technologies

- Azure Data Lake Storage (ADLS Gen2)
- Azure Databricks
- PySpark
- Delta Lake
- SQL (Window Functions, Joins, CTEs)

---

## Data Structure

- `Loan_Application_Dataset.csv`
- `Customer_Table.csv`
- `Loan_Table.csv`

Each dataset was uploaded to an Azure Storage account, then accessed securely via OAuth for processing in Databricks.

---

## What I Learned

This project helped me sharpen my understanding of:
- Managing cloud resource groups, storage accounts, and workspace configuration
- Connecting and authenticating between services securely
- Structuring pipelines for ingestion, transformation, and output
- Working with Spark SQL in a real-world financial data context

---

## Sample Output Query

```sql
SELECT 
    a.loan_id, 
    c.loan_name,
    b.customer_id, 
    b.first_name, 
    b.last_name,
    c.loan_purpose,
    c.application_date,
    c.creation_date
FROM loan_applications a
LEFT JOIN customers b ON a.customer_id = b.customer_id
LEFT JOIN loans c ON a.loan_id = c.loan_id 
ORDER BY b.first_name, b.last_name, c.application_date DESC
