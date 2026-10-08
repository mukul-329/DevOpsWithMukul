## EKS in AWS

1. How would you ensure the security of EKS cluster ?
```
I would secure an EKS cluster using defense-in-depth, covering the control plane, worker nodes, workloads, network, IAM, secrets, and supply chain.
I would use private API endpoint access where possible, EKS IAM/RBAC with least privilege, and IRSA or EKS Pod Identity so pods get only the AWS permissions they need. At the network layer, I would use private subnets, security groups, NetworkPolicies, and restricted Kubernetes API access, with AWS WAF in front of internet-facing applications.
For workloads, I would enforce Pod Security Standards, non-root containers, read-only filesystems, resource limits, image scanning with tools such as Trivy, and signed/trusted images.
Finally, I would enable CloudTrail, EKS control-plane logs, GuardDuty, Security Hub, and CloudWatch, and continuously scan the cluster and IaC for vulnerabilities and misconfigurations.
```

2. How would you secure a Pod ?
```
I would secure a pod using least privilege, container hardening, network isolation, and runtime controls.
I would run containers as a non-root user, use a read-only root filesystem, drop unnecessary Linux capabilities, disable privilege escalation, and avoid privileged containers.
I would apply Pod Security Standards and define resource requests/limits to reduce abuse and noisy-neighbor issues.
For network security, I would use Kubernetes NetworkPolicies to restrict which pods can communicate with it.
For AWS access, I would use EKS Pod Identity or IRSA with a dedicated IAM role rather than giving permissions through the node role, and I would scan/sign images using tools such as Trivy before deployment.
```
