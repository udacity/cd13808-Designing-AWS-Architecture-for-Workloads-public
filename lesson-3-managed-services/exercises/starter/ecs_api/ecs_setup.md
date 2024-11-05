# Deploying FastAPI on AWS ECS

## Prerequisites

- AWS account with access to ECS, IAM, and EC2 services.
- AWS CLI and Docker installed on your local machine.

## Step-by-Step Instructions

### Step 1: Create an IAM Role

1. **Navigate to the IAM Console:**
   - Go to the AWS Management Console.
   - Select **IAM** from the services menu.

2. **Create a Policy:**
   - Go to **Policies** and click **Create policy**.
   - Use the **JSON** tab and enter the following policy for ECS tasks:

     ```json
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Action": [
             "ec2:Describe*",
             "elasticloadbalancing:Describe*",
             "elasticloadbalancing:RegisterTargets",
             "elasticloadbalancing:DeregisterTargets",
             "elasticloadbalancing:DescribeTargetHealth",
             "elasticloadbalancing:SetRulePriorities",
             "elasticloadbalancing:ModifyRule",
             "elasticloadbalancing:ModifyListener",
             "ecs:CreateCluster",
             "ecs:DeregisterContainerInstance",
             "ecs:DiscoverPollEndpoint",
             "ecs:Poll",
             "ecs:RegisterContainerInstance",
             "ecs:StartTelemetrySession",
             "ecs:Submit*",
             "logs:CreateLogGroup",
             "logs:CreateLogStream",
             "logs:PutLogEvents"
           ],
           "Resource": "*"
         }
       ]
     }
     ```

   - Name the policy `ECSExecutionPolicy` and create it.

3. **Create an IAM Role:**
   - Go to **Roles** and click **Create role**.
   - Choose **ECS** as the service.
   - Attach the `ECSExecutionPolicy` policy.
   - Name the role `ECSTaskExecutionRole` and create it.

### Step 2: Set Up Amazon ECS

1. **Create an ECS Cluster:**
   - Navigate to the **ECS Console**.
   - Click **Clusters** and then **Create Cluster**.
   - Choose **Networking only** (for Fargate) and click **Next step**.
   - Name your cluster (e.g., `FastAPICluster`) and create it.

2. **Create a Task Definition:**
   - Go to **Task Definitions** and click **Create new Task Definition**.
   - Choose **Fargate** and click **Next step**.
   - Configure the task definition:
     - Name: `FastAPITask`
     - Task Role: `ECSTaskExecutionRole`
     - Container Definitions: Add a container with the following settings:
       - Name: `fastapi-container`
       - Image: `<your-docker-image>`
       - Port Mappings: 80 (container port)

3. **Create a Service:**
   - Go to your cluster and click **Create** under **Services**.
   - Choose **Fargate** as the launch type.
   - Select the task definition and configure the service:
     - Number of tasks: 1
     - Load Balancer: Select **Application Load Balancer** and configure it.

### Step 3: Configure the Load Balancer

1. **Create an Application Load Balancer:**
   - Navigate to the **EC2 Console** and select **Load Balancers**.
   - Click **Create Load Balancer** and choose **Application Load Balancer**.
   - Configure the load balancer:
     - Name: `FastAPILoadBalancer`
     - Scheme: Internet-facing
     - Listeners: HTTP
     - Availability Zones: Select appropriate zones

2. **Configure Target Groups:**
   - Create a new target group for the ECS service.
   - Register the ECS tasks with the target group.

3. **Update the ECS Service:**
   - Go back to the ECS Console.
   - Update the service to use the new load balancer and target group.

## Conclusion

By following these steps, you will have a FastAPI application running on AWS ECS, accessible through an Application Load Balancer.