## Senior DevOps Engineer

1. What is CI and CD (continuous delivery/deployment) ?
   ```
   CI (Continuous Integration) is the practice of frequently merging code changes into a shared repository, where automated builds and tests validate the changes.
   CD (Continuous Delivery) extends CI by automatically preparing and validating the application for release, but production deployment usually requires manual approval.
   Continuous Deployment goes one step further: every change that passes the required automated checks is deployed to production automatically, without a manual release approval.
   A typical pipeline includes code checkout, build, unit testing, code-quality checks, security scanning, artifact/image creation, deployment, and post-deployment validation. Tools such as Jenkins, GitHub Actions, GitLab CI, and Azure DevOps automate these stages, improving release speed, consistency, and reliability.
   ```

3. We have to deploy one of API, what all the requirements will you gather to deploy it on production ?
   ```
    Before deploying an API to production on AWS EKS, I would gather requirements across application, traffic, infrastructure, security, availability, observability, and deployment strategy.
    First, I would understand the API's runtime, container image, ports, dependencies, environment variables, secrets, health-check endpoints, and external integrations.
    Then I would estimate expected requests per second, peak traffic, latency targets, CPU/memory requirements, and scaling needs to size the pods and cluster appropriately.
    I would clarify the networking and exposure requirements, such as whether the API is public or internal, its custom domain, TLS certificates, CloudFront/WAF requirements, and database connectivity.
   
     - Application: Runtime, container image, ports, dependencies, API endpoints
     - Traffic: Average/peak RPS, concurrent users, payload sizes
     - Compute: Pod replicas, CPU/memory requests and limits, autoscaling
     - Networking: Public/private API, domain, DNS, ALB, CloudFront, WAF
     - Security: TLS, IAM, secrets, RBAC, image scanning, NetworkPolicies,Health	Startup, readiness, liveness probes
     - Availability: Multi-AZ deployment, replicas, disruption budgets
     - Dependencies: Database, cache, queues, third-party APIs, timeouts
     - Observability: Logs, metrics, dashboards, alerts, tracing
     - Deployment: CI/CD, approvals, rolling/canary deployment, rollback
     - Recovery: Backup requirements, RTO, RPO, disaster recovery
     - Cost: Expected AWS resource consumption and budget
   ```

4. How will you make sure of High availaibility that you have mentioned for this API deployment if deployment is done in kubernetes cluster?
   ```
   To ensure high availability (HA) for an API running on Kubernetes, I would distribute multiple replicas across at least two, preferably three, Availability Zones in AWS EKS.
   I would expose the API through an ALB deployed across multiple AZs, with a Kubernetes Service routing traffic only to ready pods. I would configure readiness, liveness, and startup probes, along with Horizontal Pod Autoscaler (HPA) to scale replicas based on CPU, memory, or application metrics. 
   I would use pod anti-affinity or topology spread constraints to avoid placing all replicas on the same node or in the same AZ, and a PodDisruptionBudget (PDB) to limit voluntary disruptions during maintenance. 
   Finally, I would make the application stateless where possible, ensure the database and other dependencies are highly available, and monitor failures with CloudWatch, Prometheus, and Grafana.
   ```
5. In case of failure in one AZ, how the traffic will shift back to another AZs ?
   ```
    Task: I need to keep the API accessible through the surviving AZs while minimizing failed requests and maintaining enough capacity.
    Action:
    - I would configure the ALB across multiple AZs and enable cross-zone load balancing where appropriate, so it can distribute traffic among healthy registered targets.
    - I would use readiness probes to ensure that unready pods are removed from the Kubernetes Service endpoints, while ALB health checks detect unhealthy targets at the load-balancer layer.
    - I would distribute replicas using topology spread constraints and maintain sufficient worker-node capacity in the surviving AZs.
    - I would configure HPA for increased demand and Karpenter or Cluster Autoscaler to add node capacity if the existing nodes cannot accommodate additional pods.
    - I would test the scenario by simulating node or workload failures and monitoring ALB target health, pod readiness, error rates, and recovery time.
   ```

6.    
