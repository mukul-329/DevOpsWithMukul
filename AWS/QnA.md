- How will you secure AWS production environment ?
```
I would secure an AWS production environment using a defense-in-depth approach across identity, network, data, workloads, monitoring, and governance.
For identity, I would use IAM least privilege, IAM roles instead of access keys, MFA, and separate production accounts using AWS Organizations/Control Tower where applicable.
At the network layer, I would use private subnets, security groups, NACLs, controlled VPC endpoints, and AWS WAF + CloudFront for internet-facing applications, while restricting administrative access through a secure path such as SSM Session Manager.
For data protection, I would enable encryption at rest with KMS, TLS in transit, secure secrets using AWS Secrets Manager/Parameter Store, and protect backups with appropriate controls.
Finally, I would implement CloudTrail, GuardDuty, Security Hub, Config, CloudWatch, centralized logging, vulnerability scanning, and CI/CD security checks so that security is continuously monitored rather than handled only during deployment.
```
