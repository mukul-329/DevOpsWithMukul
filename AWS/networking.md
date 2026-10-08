## Networking in AWS

1. How is Networking works in AWS & How multiple EC2 will communicate with each other ?
```
AWS networking starts with a VPC, which is a logically isolated network containing subnets, route tables, security groups, and network interfaces. Subnets are associated with specific Availability Zones, and EC2 instances communicate using their private IP addresses or private DNS names through the VPC's underlying network.
For EC2 instances in the same VPC, the local route in the route table allows traffic between their CIDR ranges, while Security Groups act as stateful virtual firewalls controlling which traffic is allowed.
If instances are in different VPCs, I would use connectivity such as VPC Peering, Transit Gateway, or Cloud WAN, depending on the scale and architecture.
For internet communication, traffic typically goes through an Internet Gateway for public subnets, while private instances can use a NAT Gateway for outbound internet access without becoming directly reachable from the internet.
``` 
2. What is VPC and subnets ?
```
A VPC (Virtual Private Cloud) is a logically isolated network in AWS where I define the IP address range, subnets, route tables, security groups, and network connectivity for my workloads.
A subnet is a smaller IP range carved out of the VPC CIDR and is associated with a single Availability Zone. I typically create public subnets for resources that need direct internet connectivity, such as an internet-facing ALB, and private subnets for application servers and databases.
A subnet itself is not automatically public or private; its route table determines whether it has a route to an Internet Gateway
```

3. If two EC2 instances are in the same VPC but different subnets, how exactly does the packet travel from one instance to the other?
```
When two EC2 instances are in the same VPC but different subnets, the packet is routed using the local route that AWS automatically adds to the VPC route table.
For example, if the VPC CIDR is 10.0.0.0/16, and the source is 10.0.1.10 while the destination is 10.0.2.10, the route table contains a 10.0.0.0/16 → local route, so the traffic stays within the VPC and does not go through an Internet Gateway or NAT Gateway.
The source EC2 sends the packet through its Elastic Network Interface (ENI), and AWS's VPC networking layer routes it toward the destination subnet and ENI. Before the packet is delivered, the destination Security Group must allow the traffic, and any relevant Network ACL must also permit it. So the simplified flow is EC2 → ENI → VPC local route → destination ENI → destination EC2.
```

4. What is the difference between a Security Group and Network ACL, and which one is evaluated first when traffic reaches an EC2 instance?
```
A Security Group (SG) is a stateful, instance/ENI-level firewall, while a Network ACL (NACL) is a stateless, subnet-level firewall.
Security Groups use allow rules only, and when traffic is allowed in one direction, the corresponding return traffic is automatically allowed because the SG is stateful. NACLs support both allow and deny rules, are evaluated in rule-number order, and require explicit rules for both inbound and outbound traffic.
For traffic entering an EC2 instance, the NACL is evaluated at the subnet boundary first, and then the Security Group is evaluated before traffic reaches the ENI/instance. In practice, I use NACLs for broad subnet-level guardrails and Security Groups for fine-grained workload-level access control.
```

5. Suppose users are trying to access an HTTPS application on an EC2 instance, and the EC2 Security Group allows TCP port 443, but the application is still unreachable. How would you troubleshoot it ?
```
I would first check the subnet's NACL inbound rules and verify whether TCP 443 from the client source is allowed. If the NACL has an explicit DENY that matches the traffic, the packet will be dropped at the subnet boundary and will never reach the EC2 ENI/Security Group. I would then check the NACL's outbound rules, because NACLs are stateless and the return traffic must also be explicitly allowed. Finally, I would verify the EC2 Security Group and confirm that TCP 443 is allowed from the expected source. Once the matching NACL rules and Security Group rules allow the traffic, the HTTPS request can reach the EC2 instance and the response can return successfully.
```

6. What is route table and its importance when we have NACL, SGs ?
```
A route table determines where network traffic should go, while Security Groups and NACLs determine whether that traffic is allowed.
Every subnet is associated with a route table, and the router evaluates the destination IP against the route table using longest-prefix matching to select the next hop, such as local, Internet Gateway, NAT Gateway, Transit Gateway, or VPC Peering.
For example, traffic between two subnets in the same VPC normally matches the VPC's local route, while internet-bound traffic from a private subnet can match a route to a NAT Gateway.
After routing determines the path, NACLs provide subnet-level stateless filtering and Security Groups provide stateful ENI-level filtering. So the key distinction is Route Table = where traffic goes, NACL/SG = whether traffic is permitted.
```
7. Nat Gateway vs Internet Gateway ?
```
An Internet Gateway (IGW) provides a path between a VPC and the public internet and is typically used by resources in a public subnet that have a public or Elastic IP.
A NAT Gateway allows resources in a private subnet to initiate outbound connections to the internet while preventing unsolicited inbound internet connections to those private resources.
An IGW is attached to the VPC, while a NAT Gateway is deployed in a subnet, normally a public subnet, and uses an Elastic IP for internet access. For example, a public ALB can use 0.0.0.0/0 → IGW, while private EC2 instances can use 0.0.0.0/0 → NAT Gateway → IGW.
So the key distinction is IGW provides direct internet connectivity for public resources, while NAT Gateway provides outbound internet access for private resources.
```
8. If the NAT Gateway is deployed in a public subnet, why can't a private EC2 instance simply use the Internet Gateway directly ?
```
A private EC2 instance cannot use an Internet Gateway (IGW) directly because an IGW provides internet connectivity for resources that have a publicly routable IPv4 address, such as a public IPv4 or Elastic IP.
A private EC2 instance normally has only a private IP address, which is not routable on the public internet.
The NAT Gateway acts as the intermediary: the private instance sends traffic to the NAT Gateway, which performs source NAT and uses its Elastic IP to communicate with the internet through the IGW.
The response traffic is translated back and routed to the private instance through the NAT Gateway.
Therefore, the typical flow is Private EC2 → NAT Gateway → Internet Gateway → Internet.
```

9. How would IP allocation done for resources ?
```
In AWS, I would first define a VPC CIDR block, for example 10.0.0.0/16, and then divide it into smaller subnet CIDRs, such as 10.0.1.0/24 for one subnet and 10.0.2.0/24 for another.
AWS automatically assigns private IPv4 addresses to resources such as EC2 instances through their Elastic Network Interfaces (ENIs) from the subnet's available IP range. I would use private IPs for internal communication and assign public IPv4 addresses or Elastic IPs only when a resource actually needs public connectivity.
A /24 IPv4 subnet contains 256 total addresses, but AWS reserves 5 IP addresses in every subnet, so only 251 IPv4 addresses are available for customer resources. AWS reserves the network address, VPC router address, DNS address, future use, and the broadcast address.
```

10. What is Elastic IP ?
```
An Elastic IP (EIP) is a static public IPv4 address allocated to your AWS account that you can associate with supported AWS resources, such as an EC2 instance or NAT Gateway. Unlike an automatically assigned public IPv4 address, an Elastic IP can remain the same even if the underlying resource is stopped, restarted, or replaced, depending on how it is used. I would use an EIP when an application or network component requires a stable public IPv4 address
```

