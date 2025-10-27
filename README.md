# AWS-DataLake-Pipeline

Project: AWS Data Lake Pipeline


Overview

This project demonstrates an end-to-end cloud data pipeline using AWS. The pipeline ingests raw data into Amazon S3, transforms it using AWS Glue, and enables querying with AWS Athena. It also optionally uses AWS Lambda to automate ETL jobs.
Architecture Diagram
(Optional: Insert diagram here showing S3 -> Glue -> Athena -> Redshift workflow)
Features
•	Ingest raw CSV/JSON files into S3
•	Transform and clean data with AWS Glue
•	Query transformed data using AWS Athena
•	Automate ETL jobs with Lambda triggers
AWS Services Used
•	Amazon S3
•	AWS Glue
•	AWS Lambda
•	AWS Athena
•	AWS IAM
Sample Data
Include sample CSV or JSON files in the data/ folder.
Step-by-Step Instructions
1.	Set up AWS account and IAM roles
2.	Create S3 buckets for raw and transformed data
3.	Upload sample data to the raw bucket
4.	Configure AWS Glue crawler to create a Data Catalog table
5.	Create and run AWS Glue ETL job for data transformation
6.	Query transformed data in Athena
7.	(Optional) Set up Lambda trigger for automation
Running the Project
1.	Upload new CSV/JSON files to the raw bucket
2.	Glue job will process and transform the data
3.	Query results in Athena
Output
Transformed data stored in S3 and available for querying in Athena.

Repository Structure

AWS-DataLake-Pipeline/

├── data/                # Sample CSV/JSON files

├── glue_scripts/        # Python ETL script

├── README.md            # Project documentation

└── architecture_diagram.png
