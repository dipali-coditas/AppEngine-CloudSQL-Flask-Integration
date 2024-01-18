Project App Deployment Guide Docs - App Engine 

Overview

This repository contains project-specific modifications to the main file sourced from the Google Cloud Platform Python Docs Samples repository. These changes are tailored for deploying an App Engine application in the context of our project. The following section outlines the commands utilized in the project deployment.

Deployment Commands 

1. Establishing a Connection to the Cloud SQL Instance:

gcloud sql connect [instance_name] --user=username

2. Selecting the Project Database:

use [database_name]

3. Creating a 'demo_tbl' Table in the Project Database:

create table demo_tbl(
   demo_id INT NOT NULL AUTO_INCREMENT,
   demo_txt VARCHAR(500) NOT NULL,
   PRIMARY KEY (demo_id)
);

4. Inserting a Sample Record into the 'demo_tbl' Table:

insert into demo_tbl(demo_id, demo_txt) values(1, "hello guys, thanks for being part of our project :)");

5. Retrieving Data from the 'demo_tbl' Table:

select demo_txt from demo_tbl;

6. Configuring Cloud SQL Instance Connections for the Project:

- Navigate to the Cloud SQL instance.
- Edit the Connections settings:
- Public IP -> Connections -> Authorized Networks -> Add a Network -> 0.0.0.0/0 -> Save

7. App Engine - Deploying the Project Application Using Cloud Shell :

- Add the path and navigate to the project application folder.
- Deploy the project application
- Navigate to your directory and then fire following command and wait for few minutes

gcloud app deploy

8. Final check

- Use URI and access your application

Purpose

These modifications are made to streamline the deployment process for our project. 



   




