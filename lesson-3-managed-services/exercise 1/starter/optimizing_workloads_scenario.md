# Exercise: Assessing and Optimizing Workloads

## Scenario Overview

You are tasked with assessing the performance and scalability of an existing cloud-based architecture. The architecture supports a web application that experiences variable traffic patterns, with peak loads during business hours.

### Architecture Details

- **Web Tier:**
  - **Amazon EC2 Instances:** 4 t2.micro instances running a Node.js application behind an Application Load Balancer (ALB).
  - **Auto Scaling Group:** Configured with a minimum of 2 instances and a maximum of 6 instances.

- **Database Tier:**
  - **Amazon RDS:** Single db.t2.micro instance running MySQL.
  - **Read Replicas:** None configured.

- **Storage:**
  - **Amazon S3:** Used for static content delivery.
  - **Amazon CloudFront:** Configures a content delivery network (CDN) for global distribution.

### Current Challenges

- **Performance Issues:** Users report slow response times during peak hours.
- **Scalability Concerns:** The application struggles to handle increased traffic during peak loads.
- **Cost Efficiency:** The current setup is not cost-optimized, leading to higher operational costs.

## Task

1. **Identify Bottlenecks:**
   - Analyze the architecture to identify potential bottlenecks affecting performance and scalability.

2. **Recommend Optimizations:**
   - Propose optimizations to improve performance, scalability, and cost efficiency.

3. **Justify Recommendations:**
   - Provide a rationale for each recommendation, considering the trade-offs involved.