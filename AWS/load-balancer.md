## Load Balancing in AWS
1. Why would I need to place load balancer in front of my application and how can I decide which load balancer should fit for my application ?
```
I would place a Load Balancer in front of an application to provide high availability, traffic distribution, health checks, and horizontal scalability across multiple application instances.
The choice depends mainly on the protocol, traffic pattern, routing requirements, and application architecture: ALB is best for HTTP/HTTPS applications requiring Layer 7 routing such as host-based or path-based routing, while NLB is designed for Layer 4 TCP/UDP/TLS traffic where very high performance, low latency, or static IPs are important.
Gateway Load Balancer (GWLB) is used when I need to deploy and scale network/security appliances, such as firewalls or inspection appliances.
For most modern web applications, I would start with ALB, especially when I need features like /api versus /login routing, HTTP headers, redirects, or integration with container platforms. I would make the final decision based on the application's protocol and routing requirements, not simply on expected traffic volume.
```

2. What is the difference between ALB and NLB, and when would you choose NLB over ALB?
```
The main difference is that ALB operates at Layer 7, while NLB primarily operates at Layer 4 of the OSI model. ALB understands HTTP/HTTPS and supports application-aware features such as host-based routing, path-based routing, HTTP headers, redirects, and HTTP health checks, making it suitable for web applications and APIs. NLB handles TCP, UDP, and TLS traffic and is designed for high throughput, low latency, large numbers of connections, and static IP requirements. I would choose NLB over ALB when the application is not HTTP-based, requires Layer 4 load balancing, needs static IP addresses, or requires very high-performance connection handling. If I need intelligent HTTP routing such as /api to one service and /web to another, I would choose ALB.
```

3. Can you explain how ALB distributes traffic to targets and performs health checks?
```
I would create a target group containing the application instances and configure an ALB listener on the required port, such as HTTPS 443. I would configure listener rules to determine which target group receives each request, for example using path-based routing.
I would configure an HTTP health check such as GET /health with the appropriate health-check interval, timeout, and healthy/unhealthy thresholds. The ALB would continuously evaluate the health-check responses and stop sending new requests to targets that become unhealthy.
```

4. What happens to an existing connection/request when an EC2 target behind an ALB becomes unhealthy?
 ```
I would configure an appropriate health-check endpoint so the ALB detects the failure. Once the target becomes unhealthy, the ALB stops routing new requests to that target.
For planned deregistration or deployments, I would use deregistration delay/connection draining so existing in-flight requests have an opportunity to complete.
If the EC2 instance has actually crashed and the existing TCP connection is broken, I would rely on the application's retry mechanism or client-side retry behavior rather than expecting the ALB to recover that request.
```

5. What is Auto Scaling ?
```
Auto Scaling automatically maintains and adjusts the number of EC2 instances based on application demand, availability, and configured scaling policies.
```

6. How should we design our ec2 instances if we are going to receive a high traffic from application ?
```
I would deploy multiple EC2 instances across multiple Availability Zones inside an Auto Scaling Group and place an ALB in front of them.
I would configure health checks and scaling policies based on metrics such as CPU utilization, ALB request count per target, or application-specific CloudWatch metrics.
I would make the application stateless, moving shared sessions to ElastiCache and static files to S3, where appropriate. For traffic that can be cached, I would put CloudFront in front of the application, and for expensive asynchronous operations I would introduce a queue such as SQS so traffic spikes can be absorbed.
```

7. What is Auto Scaling and the default behaviour of auto scaling groups or the instances inside that group ?
```
Amazon EC2 Auto Scaling automatically maintains and adjusts the number of EC2 instances based on application demand, availability, and configured scaling policies.
An Auto Scaling Group (ASG) manages instances using a Launch Template, minimum capacity, desired capacity, and maximum capacity. By default, an ASG maintains its desired capacity, launches replacement instances when an instance becomes unhealthy, and attempts to distribute instances evenly across configured Availability Zones.
By default, EC2 status checks determine instance health, while ELB health checks must be explicitly enabled if we want load-balancer health to affect instance replacement. Importantly, an ASG does not automatically scale based on CPU or traffic unless we configure Target Tracking, Step Scaling, Scheduled Scaling, or Predictive Scaling policies.
```

8. What is the difference between vertical scaling and horizontal scaling, and why is horizontal scaling generally preferred in a production environment?
```
Vertical scaling means increasing or decreasing the capacity of an existing instance, such as moving from m6i.large to m6i.xlarge, while horizontal scaling means adding or removing multiple instances to handle the workload.
Horizontal scaling is generally preferred for production because it provides better high availability, fault tolerance, elasticity, and zero/small-downtime scaling when combined with an ALB and Auto Scaling Group.
With horizontal scaling, an individual instance can fail without necessarily taking down the application because traffic can be routed to other healthy instances.
Vertical scaling has limits because every instance has a maximum CPU, memory, network, and storage capacity, and changing the instance type can require replacing or restarting the instance.
I would therefore use horizontal scaling as the primary strategy, while vertical scaling can still be useful when the application has a resource bottleneck that cannot easily be distributed.
```

9. what is placement group and why it is important to have ?
```
An EC2 Placement Group is a logical grouping that lets you control how EC2 instances are physically positioned within AWS infrastructure to optimize for performance, latency, or fault isolation. AWS provides three main strategies:-
- Cluster, which places instances close together for high network throughput and low latency
- Spread, which places instances on distinct underlying hardware to reduce correlated failures
- Partition, which separates instances into partitions so a hardware failure affects only one partition.
I would use Cluster for tightly coupled workloads such as HPC or distributed computing, Spread when individual instance failure isolation is critical, and Partition for large distributed systems such as Kafka or Hadoop. Placement groups are not something every production application needs; I would choose one when the workload has a specific network-performance or fault-isolation requirement.
```
