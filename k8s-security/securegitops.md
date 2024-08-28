#Secure GitOps Room

## Task 2

The first actionable task of the room describes the foundational concepts of GitOps which are:
- Declarative Configuration
- Automation
- Version Control
- Observability

It also goes over two of the foundational GitOps tools both are listed below and reference to the core concepts pages for each tool.
- [ArgoCD] (https://argo-cd.readthedocs.io/en/stable/core_concepts/)
- [Flux] (https://fluxcd.io/flux/concepts/)


## Task 3

This task covers the importants of kubernetes in GitOps. The ability to scale, load balance, and monitor health are key in making it the preferred engine for GitOps

## Task 4

This task highlighted the big challenges of each of the components of GitOps noting that with the benefits, comes challenges.

- Argo Challenges
    - Access Controls
    - Secrets Management
- K8s Challenges
    - Secure cluster configuration
    - Container image vulnerability management
- GitHub Challenges
    - Plain Text secrets in commit history
    - Vulnerable source code
    - Dependency management/software bill of materials

References
- [Container Security Contexts] (https://www.aquasec.com/cloud-native-academy/kubernetes-in-production/kubernetes-security-context/)
- [K8 Security Best Practices] (https://tryhackme.com/r/room/k8sbestsecuritypractices)


## Task 5

This task goes into applying some of what we gathered about Argo CD specifically. Once the machines and Attack Box have both been spun up you'll be able to hit the Argo server via the browser in the AttackBox

The first question required information on visually what happens when you have clicked the "sync" button. 
when the deployment hasn't been synced with the source code repository commit.

The next two questions can be answered by looking through the security context template and using the description in the task of what each of the entries in that template file means or controls within thethe scope of the deployment.

In order to find the Kernel version, I used the grid view that had the option of navigating into the logs of the start up of the node. In those logs searched for OS and the kernel version was closely behind that 

Last question can be answered by using the git commit details from the very first view of the Argo deployment. Commit hashes are very distinctive and not hard to pick out from the UI also you can hover over the hyperlinks and see the tooltip actually make reference to the git repository the commit comes from.