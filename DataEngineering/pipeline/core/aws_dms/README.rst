AWS DMS - Database Migration Service
      easily and securely migrate and replicate your databases and data warehouse to AWS

SCT  - Schema Conversion Tool -  convert your and Copy Schema  (DDS language such as UDF, indexes, functions, store procedures, trigger) from native/source databases to destination DB
                      https://aws.amazon.com/marketplace/search/results?searchTerms=Workload+Qualification 
                               AWS native service as Amazon  Aurora and Redishift 
       Tool from AWS => Workload Qualification Framework found in the  AWS Marketplace
                         WQF automatically generates the following reports:
                        • Workload assessment based on the complexity, size, and technology used
                        • Recommendations on migration strategies to migrate to Amazon RDS or Amazon Aurora
                        • Actionable feedback and step-by-step instructions for migrations
                        • Assessment of the migration effort required based on team size and member roles

       Modernized =>  Moving Old database move to a mysql or Postgress
       Migrate    => Move SQLserver DW to more cost effective DW  like Redishift
       Repliction  =>  copy data from one data store to another

DMS  Support
    Migration VAlidation
         - Data Type VAlidation
         - Post Migration Assessment

<<<<<<< HEAD
=======================
Setup Migration Process
=======================
https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Installing.html


step 1:  Download  the compressed file that contains the AWS SCT installer, => https://s3.amazonaws.com/publicsctdownload/Ubuntu/aws-schema-conversion-tool-1.0.latest.zip
         using the link for your operating system. All compressed files have a .zip extension. 
         aws-schema-conversion-tool-1.0.build-number.deb
         When you extract the AWS SCT installer file, it will be in the appropriate format for your operating system. 
        - Extract the AWS SCT installer file for your operating system, shown following.
          Operating system 	File name
          Ubuntu Linux
          
        - Download respective jdbc for source and target

Step 3: Setup taget database and DMS security group for connection over the public Internet
         - Configure the security group  Reolication DMS
           Set outbound traffic from DMS Replication instance for ingestion to target RDS Database
           with Outbound set to all traffic ip 0.0.0.0
         - Create security group for the target database 
           Set inbound traffic Ip to the Outbound security group created in the first line above
           Set port to 5432 for Postgres

Step 4 : Run the AWS SCT installer file extracted in the previous step. 
         - Use the instructions for your operating system, shown following. 
            >>> sudo dpkg -i aws-schema-conversion-tool-1.0.build-number.deb
         - Ensure AWS CLI is Configure
         - Configure your AWS credentials connetions on the SCT 
         - add DB Source connection details




=======
    CDC : Change Data Capture on Transaction log and its eventual consistence  , note this not an instance  
    Clone/Replication : Ability to clone or replicate a database fapplication test on for prod/Stage prototype
    Security : Encrypt that in trasmission with SSL/TLS and at rest with encrytion with KMS for masking.
>>>>>>> refs/remotes/origin/main

===================
AWS DMS + Snowball
=====================
    Snowball => Is a phyiscal hardware available from aws which can be used to load a very High volume of data from your pysical premise 
     Reasons :
       - Migrating Large databases (Over 5TB) 
       - Migrate over slow network
       - Migrate many database at once
       - A full dumb of database to Snowball load  which is then loaded into s3 and a restore can be done with DMS


Dms trust policy  to be add to IAM role
=============== =======================
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "dms.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}