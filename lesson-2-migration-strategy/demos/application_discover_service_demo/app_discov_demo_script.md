# Demo: Using AWS Application Discovery Service for Migration Planning

## Introduction

In this demo, we'll walk through the process of using AWS Application Discovery Service to gather information about our on-premises applications before migrating them to AWS. We have three sample applications:

1. A simple API
2. A data processing function
3. A scheduled job

## Step 1: Install and Configure the AWS Application Discovery Agent

1. Log in to your on-premises server where the applications are running.

2. Download the AWS Application Discovery Agent:

```bash
wget https://s3.amazonaws.com/aws-discovery-agent/linux/latest/aws-discovery-agent.tar.gz
```


3. Extract and install the agent:

```bash
tar -xzf aws-discovery-agent.tar.gz
sudo bash install
```


4. Configure the agent with your AWS credentials and the desired AWS region:
```bash
sudo /opt/aws/discovery/bin/configure-agent
```

## Step 2: Start Data Collection
  1. Start the Discovery Agent:
    ```bash
    sudo /etc/init.d/aws-discovery-daemon start
    ```
  2. Verify that the agent is running:
    ```bash
    sudo /etc/init.d/aws-discovery-daemon status
    ```  

## Step 3: Run the Applications
  1. Start the Flask API:
    ```bash
    python app_discov_api.py
    ```
  2. Run the data processing script:
    ```bash
    python app_discov_dp.py
    ```
  3. Start the scheduled job:
    ```app_discover_de.py
    ```
    

Let the applications run for a while to allow the Discovery Agent to collect data.

## Step 4: View and Analyze the Collected Data

1. Open the AWS Management Console and navigate to the AWS Application Discovery Service.

2. Click on "Data Collectors" to verify that your agent is connected and actively collecting data.

3. Go to the "Discovered servers" section to see information about your on-premises server.

4. Click on your server to view detailed information, including:
- Server specifications (CPU, memory, disk)
- Network connections
- Processes running on the server

5. Navigate to the "Discovered processes" section to see information about the Python processes running your applications.

6. Use the "Network connections" view to understand the communication patterns between your applications and any external dependencies.

## Step 5: Generate Migration Reports

1. In the AWS Application Discovery Service console, go to the "Migration evaluator" section.

2. Click on "Create assessment report" to generate a report based on the collected data.

3. Review the report to get insights on:
- Server utilization
- Potential AWS instance types for migration
- Estimated AWS costs

## Step 6: Plan Your Migration

Based on the collected data and generated reports:

1. Identify the AWS services suitable for each application:
- App 1 (API): Consider using Amazon ECS or AWS App Runner
- App 2 (Data Processing): Look into AWS Lambda or AWS Glue
- App 3 (Scheduled Job): Evaluate AWS Lambda with EventBridge

2. Determine the appropriate instance types and sizes for your applications.

3. Identify any dependencies or network configurations that need to be addressed during migration.

4. Create a migration strategy and timeline based on the insights gained from the Application Discovery Service.

## Conclusion

By using AWS Application Discovery Service, we've gathered valuable information about our on-premises applications, their resource usage, and network dependencies. This data will help us make informed decisions when planning and executing our migration to AWS, ensuring a smooth transition and optimal resource allocation in the cloud environment.
