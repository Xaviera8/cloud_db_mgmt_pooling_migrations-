# cloud_db_mgmt_pooling_migrations

## Connection Pooling Setup:
### Azure:
Create a flexible server under Azure Database for Mysql
Set the compute size to Standard_B1s and the Firewall rules click, + Add 0.0.0.0 - 255.255.255.255 set max_connections to 20 and connect_timeout to 3

### GCP:
Create a MySQL instance with the enterprise edition and sandbox preset with a shared core and 1 vCPU, 0.164GB. In Network put Allow-All and set 0.0.0.0/0

Database Schema and Data:

My database has two tables (patients and medical_records). The module Faker was used to populate the tables with data.

## ERD:
Used MySQL workbench and established a connection to my datbases. Reverse engineered to generate ERDs.

## Flask: 
My application was based off of the previous assignments that we have completed and modified with the current parameters. 


## Migrations with Alembic:

terminal -> alembic init migrations
change values for sqlalchemy.url = mysql+mysqlconnector://username:password@host/database_name
alembic revision --autogenerate -m "create tables" to create a migration
alembic upgrade head
alembic upgrade head --sql > migration.sql 
   
