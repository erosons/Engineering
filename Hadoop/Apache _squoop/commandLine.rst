        

   User ==> CommandLineInterface (SQUOOP) ==> mapredOps(underHoop) ==> Hadoop   
   https://blogs.apache.org/sqoop/mediaresource/a04e8f6f-4d1e-4ee9-b726-af4e078599cf

=====================
Squoop Import Command
======================
Full extract

sqoop import \
--connect 'jdbc:sqlserver://localhost:1433;databasename=AdventureWorksDW2019' \
--table DimCustomer \
 --username sa \
 --password  \
 --target-dir /AdventureWorks20191 \
 -m 2  ;

=================
postgres
====================
 sqoop import \
--connect 'jdbc:postgresql://174.0.0.0:5432/postgres' \
--table employee \
 --username p \
 --password p \
 --target-dir /postgresTable \
 -m 100  ;


==============================
Full load with Filter Criteria
==============================

sqoop import \
--connect jdbc:mysql://localhost/userdb \
--username root \
--table emp_add \
--num-mappers or -m 1 \
--where “city =’sec-bad’” \
--target-dir /hadoop-path

================
Incremental Load
================
sqoop import \
--connect jdbc:mysql://localhost/userdb \
--username root \
--table emp \
--m 1 \
--incremental append \
--check-column id \
--last value 1205
--target-dir /hadoop-path

================
Listing databases
================
sqoop list-databases 
--connect 'jdbc:sqlserver://localhost:1433 
--username sa 
--password <password>;


================
Listing tables
================
sqoop list-tables 
--connect 'jdbc:sqlserver://localhost:1433;databasename=AdventureWorksDW2019' 
--username sa 
--password <password>;


=======================================
Exporting from hadoop to RDBMS
======================================

sqoop export \
--connect jdbc:mysql://localhost/userdb \
--username root \
--table emp \
--password \
--m 1 \
--export /hadoop-path


==============================
Exporting with Filter Criteria
==============================

sqoop export \
--connect jdbc:mysql://localhost/userdb \
--username root \
--table emp \
--password \
--where “city =’sec-bad’” \
--m 1 \
--export /hadoop-path

sqoop import \
--connect 'jdbc:sqlserver://localhost:1433;databasename=AdventureWorksDW2019' \
--table DimCustomer \
 --username sa \
 --password  \
 --target-dir /AdventureWorks20191 \
 -m 2  ;
