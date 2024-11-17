# Deploying FastAPI on AWS ECS

# Environment Setup 

## VPC Setup
- In the course repo, a cloudformation file has been provided for you (ecs-exercise-setup.yaml).
- This CloudFormation file will create a VPC that you will deploy your ECS cluster to.
- To run this file 
   - Open the Cloud9 terminal 
   - Navigate to the directory containing the `ecs-exercise-setup.yaml` file
   - Run the following command: `aws cloudformation create-stack --stack-name ecs-exercise-setup --template-body file://ecs-exercise-setup.yaml --capabilities CAPABILITY_NAMED_IAM`
- You can check on the progress two ways:
   - Navigate to the CloudFormation UI in the AWS Console
   - Run the following command in the cloud9 console and observer the "StackStatus" value: `aws cloudformation describe-stacks --stack-name ecs-exercise-setup`

## Containerizing the API and Pushing to ECR
1. Open the Cloud9 terminal
2. Navigate to the directory containing the `Dockerfile` and `fastapi_app.py` files
3. Run the following command: `docker build -f ECS-Exercise.Dockerfile -t ecs-exercise-app .`
4. Create an ECR repository: `aws ecr create-repository --repository-name ecs-exercise-app-<add your initials in lower case>`
5. Authenticate Docker to your ECR registry: `aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.<your-region>.amazonaws.com`
   - **Note:** Your account ID and region can be found in the top right of the AWS Console.
6. Tag your image with the ECR repository URI: `docker tag ecs-exercise-app:latest <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/ecs-exercise-app:latest`
7. Push the image to ECR: `docker push <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/ecs-exercise-app-<your-initials>:latest`

## Completing the Exercise

### Containerize the API and Push to ECR 
1. Open the Cloud9 terminal
2. Navigate to the directory containing the `ECS-Exercise.Dockerfile` and `fastapi_app.py` files
3. Run the following command: docker build -f ECS-Exercise.Dockerfile -t ecs-exercise-app . .
4. Create an ECR repository: `aws ecr create-repository --repository-name ecs-exercise-app-<ADD YOUR INITALS IN LOWERCASE>`
5. Authenticate Docker to your ECR registry: `aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.<your-region>.amazonaws.com`
   - **Note:** Your account ID and region can be found in the top right of the AWS Console.
6. Tag and push the image to ECR: `docker tag ecs-exercise-app:latest <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/ecs-exercise-app-<your-initials>:latest`
7. Push the image to ECR: `docker push <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/ecs-exercise-app-<your-initials>:latest`

### Create an IAM Role

- In this exercise we will turn our simple FastAPI app into an ECS task, enabling elasticity, resiliency and more. 
- For our first step, we'll create a "Task Execution Role" which will enable the API to access other AWS services like load balancers.

To create the task execution role, follow the below steps:

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

   - Name the policy `ECSExerciseExecutionPolicy` and create it.

3. **Create an IAM Role:**
   - Go to **Roles** and click **Create role**.
   - Choose **ECS** as the service.
   - Attach the `ECSExecutionPolicy` policy.
   - Name the role `ECSTaskExecutionRole` and create it.

### Set Up Amazon ECS

1. **Create an ECS Cluster:**
   - Navigate to the **ECS Console**.
   - Click **Clusters** and then **Create Cluster**.
   - Name your cluster `ECSExerciseCluster` 
   - Ensure `Fargate` is Selected for infrastructure.
   - Click `Create`

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

### Configure the Load Balancer

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

### Test the API

1. Navigate to the ECS Console and select the `ECSExerciseCluster` cluster.
2. Select the `ECSExerciseService` service.
3. Select the `ECSExerciseAPITask` task definition.
4. Select the `ECSExerciseContainer` container.
5. Click on the `ecs-exercise-app` task.
6. Click on the `80` port.
7. You should see a response from the API.

## Conclusion

By following these steps, you will have a FastAPI application running on AWS ECS, accessible through an Application Load Balancer.