## Senior DevOps Engineer

1. What is CI and CD (continuous delivery/deployment) ?

2. We have to deploy one of API, what all the requirements will you gather to deploy it on production ?

3. How will you make sure of High availaibility that you have mentioned for this API deployment if deployment is done in kubernetes cluster?
   ```
   To ensure high availability (HA) for an API running on Kubernetes, I would distribute multiple replicas across at least two, preferably three, Availability Zones in AWS EKS.
  I would expose the API through an ALB deployed across multiple AZs, with a Kubernetes Service routing traffic only to ready pods. I would configure readiness, liveness, and startup probes, along with Horizontal Pod Autoscaler (HPA) to scale replicas based on CPU, memory, or application metrics. 
  I would use pod anti-affinity or topology spread constraints to avoid placing all replicas on the same node or in the same AZ, and a PodDisruptionBudget (PDB) to limit voluntary disruptions during maintenance. 
  Finally, I would make the application stateless where possible, ensure the database and other dependencies are highly available, and monitor failures with CloudWatch, Prometheus, and Grafana.
   ```
4. In case of failure in one AZ, how the traffic will shift back to another AZs ?
   ```
   Task: I need to keep the API accessible through the surviving AZs while minimizing failed requests and maintaining enough capacity.
   Action:
   - I would configure the ALB across multiple AZs and enable cross-zone load balancing where appropriate, so it can distribute traffic among healthy registered targets.
   - I would use readiness probes to ensure that unready pods are removed from the Kubernetes Service endpoints, while ALB health checks detect unhealthy targets at the load-balancer layer.
   - I would distribute replicas using topology spread constraints and maintain sufficient worker-node capacity in the surviving AZs.
   - I would configure HPA for increased demand and Karpenter or Cluster Autoscaler to add node capacity if the existing nodes cannot accommodate additional pods.
   - I would test the scenario by simulating node or workload failures and monitoring ALB target health, pod readiness, error rates, and recovery time.
   ```

5.    
