## EC2 in AWS

1. How can we ensure EC2 High availaibility ?
```
I would deploy multiple EC2 instances across at least two Availability Zones using an Auto Scaling Group.
I would place an ALB in front of the instances and configure health checks so unhealthy instances are automatically removed from traffic and replaced by the ASG.
I would make the application stateless and move persistent data to highly available services such as RDS Multi-AZ or S3, depending on the data type. I would also configure CloudWatch alarms and monitoring for CPU, memory/application metrics, instance health, ALB errors, and latency.
```

2. If one entire Availability Zone goes down, how would your EC2 Auto Scaling architecture continue serving traffic?
```
I would design the Auto Scaling Group across multiple Availability Zones, with sufficient capacity distributed across at least two or preferably three AZs. An ALB spans the configured AZs, performs health checks, and stops routing traffic to targets in the failed AZ when they become unhealthy.
The ASG detects the capacity loss and launches replacement instances in the remaining healthy AZs, subject to the configured min/desired/max capacity and available capacity.
I would also ensure the application is stateless and its data layer is highly available, such as RDS Multi-AZ, so the surviving application instances do not depend on resources in the failed AZ.
The key is that AZ failure should be treated as an expected failure scenario, with enough headroom and cross-AZ capacity to maintain the required service level.
```

3. How can we secure EC2 instance ?
```
I would place the instances in private subnets and configure security groups so only required application traffic is allowed from trusted sources such as the ALB.
For administration, I would use SSM Session Manager rather than exposing SSH publicly.
I would deploy a hardened AMI, apply regular OS security patches, remove unnecessary services, and use Amazon Inspector for vulnerability assessment.
I would enable EBS encryption with KMS, store secrets in Secrets Manager, and enable CloudTrail, GuardDuty, and CloudWatch for auditing and monitoring.
```

4. How would you secure the SSH access to an EC2 instance if Session Manager is not available?
```
If SSM Session Manager is available, I would give the EC2 instance the required IAM role and create the necessary VPC endpoints for Systems Manager, allowing the instance to communicate with the AWS Systems Manager service without requiring public internet access. I would then use Session Manager from my workstation, so I don't need SSH or a bastion host.
If Session Manager isn't available and I specifically require SSH, I would establish administrator connectivity through a VPN/private network or use a bastion host, with the EC2 security group allowing port 22 only from that trusted source.
I would never assume that a VPC endpoint itself provides a path from my laptop to the EC2 instance.
```

5. what is the defference betweem reboot and hibernate instance state ?
```
Reboot restarts the operating system on the same EC2 instance, similar to restarting a physical server, while Hibernate saves the instance's RAM state to the root EBS volume and then stops the instance.
After hibernation, when the instance starts again, the OS can resume from the saved RAM state instead of performing a normal fresh boot. With a reboot, instance memory is cleared, but with hibernation, applications and processes can resume from their previous in-memory state, subject to the workload and supported configuration.
Both operations preserve the instance identity and attached EBS data, but hibernation has additional requirements and is supported only for certain instance types, operating systems, and root EBS configurations.
I would use reboot for normal OS/application restarts and hibernate when I specifically need to preserve the in-memory state and the workload supports hibernation.
```



