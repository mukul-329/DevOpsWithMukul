# What is GitLab?
GitLab is a DevSecOps platform that provides source code management, Git repositories, merge requests, CI/CD, artifact management, security scanning, release management and deployment capabilities in one platform.

In a release management environment, I would use GitLab not only for source control but also to enforce the complete flow from code change to controlled production release.

 ```
 Organisation Account -> Groups -> Projects -> Repository
 ```
- A group is a higher-level organizational boundary used to manage multiple projects.
- A project is the repository/application boundary.
- Access Management for project:-
     - Guest: No code access, only comment and read issues, epics.
     - Reporter: View code only. Create issues and reports.
     - Developer: Code access, create branch, MRs, run pipelines but cannot manage project settings.
     - Planner: View code only. Create and manage issues, epics etc.
     - Security Manager: maintain security features
     - Maintainer: Push code. Manage branches, merge requests, CI/CD settings, and members. Cannot delete the project.
     - Owner: Full control of project settings.

  #### QnA: Developer vs Maintainer??
  - Developer is primarily responsible for development activities, while Maintainer has broader administrative and repository-management responsibilities, including CI/CD configuration, branch management and project settings.

GitLab Runners:
- GitLab Runner is the execution agent that actually runs CI/CD jobs defined in the GitLab pipeline.
    ```
    GitLab
     │
     │ assigns job
     ↓
    GitLab Runner
     │
     ├── Build
     ├── Test
     ├── Scan
     └── Deploy
    ```
- Types:
    - Instance runner: Available across gitlab instance.
    - Group runner: Dedicate to all projects within groups or subgroups.
    - project runner: Dedicated to specific project
- Runner executer:
    - Shell: Runs directly on server.
    - Docker: Run inside container.
    - Kubernetes: Each job can execute in a Kubernetes environment.
