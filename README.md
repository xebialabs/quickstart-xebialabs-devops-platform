# quickstart-xebialabs-devops-platform
## XebiaLabs DevOps Platform on AWS

### License
This Quick Start is distributed under the Apache License, Version 2.0. This Quick Start uses "psycopg2" library, which is provided under the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

### Overview
This Quick Start automatically deploys the XebiaLabs DevOps Platform into a new or existing virtual private cloud (VPC) on the Amazon Web Services (AWS) Cloud in about 40 minutes. The Quick Start includes AWS CloudFormation templates and a deployment guide with step-by-step instructions.

The XebiaLabs DevOps Platform orchestrates releases by defining and automating the steps in your software delivery pipeline, connecting AWS directly to the continuous integration and continuous delivery (CI/CD) pipeline and to common development tools like Jenkins, Atlassian Jira, and JFrog Artifactory. Based on your infrastructure and application configurations, the platform dynamically generates provisioning and deployment plans for AWS Cloud, private cloud, and hybrid cloud environments.

XebiaLabs creates efficient, repeatable, scalable release and deployment processes for varied technologies, from mainframes and middleware to containers and microservices. XebiaLabs also supports deployments to many AWS products and services, such as Amazon Elastic Container Service (Amazon ECS), Amazon Elastic Container Service for Kubernetes (Amazon EKS), AWS Fargate, and AWS Service Catalog. 

This Quick Start is for development teams, infrastructure architects, and DevOps professionals who want to get started quickly with the XebiaLabs DevOps Platform for release orchestration and deployment automation.
![Quick Start architecture for the XebiaLabs DevOps Platform on AWS](https://d1.awsstatic.com/partner-network/QuickStart/datasheets/xebialabs-devops-platform-on-aws-architecture.078426cef063c8ce9d05ef3702ed565d94c822aa.png)

For architectural details, best practices, step-by-step instructions, and customization options, see the [deployment guide]( https://fwd.aws/YWarg).

#### Contributing :
In quickstart-xebialabs-devops-platform, we are using VPC and Bastion Host submodules from different repositories. git clone those submodules locally using following command:

git clone --recurse-submodules git@github.com:xebialabs/quickstart-xebialabs-devops-platform.git

To post feedback, submit feature ideas, or report bugs, use the **Issues** section of this GitHub repo.

If you'd like to submit code for this Quick Start, please review the [AWS Quick Start Contributor's Kit](https://aws-quickstart.github.io/).
