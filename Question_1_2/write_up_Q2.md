### Question 2
Caveat: first time writing terraform scripts ever.

###### Part 1 (Code/Assumptions)
Working with Amazon ECS orchestration service. Must first define the task definition (protenusApp.json.tpl) and then the service definition (protenusApp.tf). The task definition describes which docker container to run on ECS (i.e. a docker container pulled from ECR). The service definition runs a specific number of containers based on the task definition. AWS ECS manages each instance of the cluster to which the containers are deployed at the OS level. 

Assumptions:
* Docker image is created from Dockerfile and uploaded to Amazon EC2 Container Registry
* AWS IAM roles/permissions are configured for the ECR and ECS services (not configured)
* Important to configure auto-scaling and logging to CloudWatch (not configured)

###### Part 2 (Traffic Flow)
Elastic Load Balancer will direct traffic to different instances within the cluster. CloudWatch alarms will trigger autoscaling up policy when CPU metrics exceed threshold; CloudWatch alarms will triger autoscaling down policy when CPU metrics fall below threshold.

###### Part 3 (Security)
Enforce encryption of data at rest and in transit. For example if data is stored on S3, encryption at rest has three options to manage private keys: use S3 managed keys, AWS Key Management Service (KMS), use customer provided keys. Encryption at rest is also supported for RDS if data is stored in a database. Encrypting the database instance automatically encrypts the data stored within the db. For data in trasit, use SSL/TLS encryption.

###### Part 4 (Monitoring/SLAs)
Ensure that logging is enabled for the application and that metrics are collected by CloudWatch for monitoring. Establish baselines. Ensure that SLAs are met by monitoring application 1) latency, 2) traffic, 3) errors and 4) saturation (the four most important metrics according to the Google Site Reliability Engineering book).

