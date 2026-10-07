## Quiz on AWS

1. How will you secure AWS production environment ?
```
I would secure an AWS production environment using a defense-in-depth approach across identity, network, data, workloads, monitoring, and governance.
For identity, I would use IAM least privilege, IAM roles instead of access keys, MFA, and separate production accounts using AWS Organizations/Control Tower where applicable.
At the network layer, I would use private subnets, security groups, NACLs, controlled VPC endpoints, and AWS WAF + CloudFront for internet-facing applications, while restricting administrative access through a secure path such as SSM Session Manager.
For data protection, I would enable encryption at rest with KMS, TLS in transit, secure secrets using AWS Secrets Manager/Parameter Store, and protect backups with appropriate controls.
Finally, I would implement CloudTrail, GuardDuty, Security Hub, Config, CloudWatch, centralized logging, vulnerability scanning, and CI/CD security checks so that security is continuously monitored rather than handled only during deployment.
```
2. How would you secure access to a private EC2 instance without opening port 22 to the internet?
```
I would use AWS Systems Manager Session Manager to access a private EC2 instance without exposing SSH port 22 to the internet.
The EC2 instance would have an appropriate IAM instance profile, and I would provide network connectivity to Systems Manager through VPC endpoints such as ssm, ssmmessages, and ec2messages where required by the chosen Systems Manager connectivity path.
I would keep the instance in a private subnet with no public IP and restrict its security group to only the application and required internal traffic.
For auditing, I would enable CloudTrail and configure Session Manager logging to CloudWatch Logs or S3, with appropriate encryption using KMS.
This gives me controlled, auditable administrative access without maintaining bastion hosts or exposing SSH to the public internet.
```

3. How would you access an production application deployed in private ec2 instance ?
```
If the application is in a private EC2 instance, I would not expose the EC2 directly to the internet.
For a user-facing application, I would place an Application Load Balancer (ALB) in public subnets and configure the private EC2 instances as its target group, with security groups allowing traffic only from the ALB.
For a more secure architecture, I would place CloudFront + AWS WAF in front of the ALB for TLS termination, caching, and web-application protection.
For administrative access, I would use AWS Systems Manager Session Manager rather than exposing SSH port 22.
```

4. Why would we need WAF in front of load balancer, will WAF also supports DDOS protection, if not, how can we enable DDoS protection ?
```
We put AWS WAF in front of the load balancer mainly to protect the application at Layer 7, for example against SQL injection, XSS, malicious HTTP requests, bots, and rate-based attacks.
AWS WAF is not a complete DDoS protection service; AWS provides baseline DDoS protection through AWS Shield Standard, which is automatically included for AWS services such as ALB and CloudFront.
For stronger protection against large or sophisticated attacks, I would use AWS Shield Advanced, which provides enhanced DDoS detection and mitigation and additional protections for supported resources.
For a production web application, a common architecture is Route 53 → CloudFront + AWS WAF → ALB → private EC2, with Shield providing DDoS protection at the AWS edge. The important distinction is WAF = application-layer security, while Shield = DDoS protection.
```
