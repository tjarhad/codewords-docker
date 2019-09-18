---
title:  "Docker: A Practical Guide"
keywords:
- docker 
- devops

author:
- Anand Tripathi
- Tushar Jarhad
date:
- September 17, 2019
theme: 
- CambridgeUS
navigation:
- horizontal

---

# Introduction {data-background-image="images/redPanda_background.png"}

# Why Docker? {data-background-image="images/docker_icon.png" data-background-opacity=0.8 data-background-size="400px" data-background-position="left 3em bottom 0px"}

## Problems 

- Works On Machine
- Application Deployment 
- Configuration Management 
- Continuous Delivery
- Scaling Application
- Rolling Back Deployment

## Divergent

- Manual configuration 
- Shell scripts
- apt, yum, pacman


## Convergent

- Puppet, Chef, Ansible
 
## Congruent

- Docker


# Virtualisation and Containerisation 

## 

![VM Structure](images/vm-structure.png)

## 

![Container Structure](images/container-structure.png)

## LXC

- namespace
- cgroups
- chroot


# Setup

## Ubuntu

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg \ 
| sudo apt-key add -

sudo apt-get install \
software-properties-common \
python-software-properties

sudo add-apt-repository \
"deb [arch=amd64] 
https://download.docker.com/linux/ubuntu 
$(lsb_release -cs) stable"

sudo apt-get update
apt-cache policy docker-ce
sudo apt-get install -y docker-ce
sudo usermod -aG docker ${USER}
#Logout user and Login again
```

## Hello World

```bash
docker run hello-world
```


# Docker Terminology

## 

- *Image*: An image is an executable package that includes everything needed to run an application--the code, a runtime, libraries, environment variables, and configuration files.
- *Container*: A container is a runtime instance of an image--what the image becomes in memory when executed (that is, an image with state, or a user process). You can see a list of your running containers with the command, docker ps, just as you would in Linux.
- Registry: 

## Demo: Greeting

Create docker image which *cats* a file

```bash
#Build docker Image 
docker build -t greeting .
#List image
docker image ls
#List containers 
docker container ls
```


::: notes

Demo docker greeting image

:::

## 

![Docker Architecture](images/docker_architecture.png)

# Dockerfile

## Dependencies

::: notes

[Dockerfile reference](https://docs.docker.com/engine/reference/builder/)

:::




## Docker build context

- *.dockerignore* file

## Caching

- Less steps

::: notes

[Best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

:::

## MultiStage Build

::: notes

[MultiStage Build](https://docs.docker.com/develop/develop-images/multistage-build/)

:::

## Storing Metadata

```bash 
docker build -t <image> \
--build-arg GIT_TAG=$(echo "$(git rev-parse \
--abbrev-ref HEAD) \
"_"$(git rev-parse --short HEAD)") .\

```

## ARG and LABEL

```
ARG GIT_TAG=unspecified
LABEL git_tag=$GIT_TAG
```

::: notes

Show using inspect command

ARG variables are not persisted into the built image as ENV variables are. However, ARG variables do impact the build cache in similar ways. If a Dockerfile defines an ARG variable whose value is different from a previous build, then a “cache miss” occurs upon its first usage, not its definition. In particular, all RUN instructions following an ARG instruction use the ARG variable implicitly (as an environment variable), thus can cause a cache miss. All predefined ARG variables are exempt from caching unless there is a matching ARG statement in the Dockerfile.

:::


## Docker RUN


::: notes

Host binding for volume and port

:::

## Exercise

Objective: Dockerise Reactjs app.

## Dockerise React App

- Dependency to build Reactjs App
- How to serve build over http?

## Persistance

## Code mount vs Code add

## Container should be stateless

::: notes

Possible Break 

:::


# Docker Compose file

## 


::: notes

[Compose file reference](https://docs.docker.com/compose/compose-file/)

:::

## Address resolution

## Process Manager

Avoid using process manager like 
python supervisor,pm2 inside docker

# Automation

## QA Automation

![selenium/hub](images/qa_automation.png)

## CI Pipeline

![docker ci](images/docker_ci.png)

## Useful Images

- Portainer
- pmsipilot/docker-compose-viz
- dockersamples/visualizer


# In Production

## Clean up Tasks

```bash
#Delete every container
docker rm -f $(docker ps -a -q)
# Delete every Docker image
docker rmi -f $(docker images -q)
#Remove Dangling images
docker rmi $(docker images -f "dangling=true" -q)
# Remove all untagged images
docker image rm -f \
$(docker image ls | grep "^<none>" | awk "{print $3}")
```

## Monitoring (Telemetry)

- [Configure logging drivers](https://docs.docker.com/config/containers/logging/configure/)
- [Collect Docker metrics with Prometheus](https://docs.docker.com/config/thirdparty/prometheus/)

## Warnings!

- Check host file system driver support for docker.
- Test kernel support of docker on cloud provided OS.
- Avoid production database using docker.
- Save build image to cloud

::: notes

- Ideally use ext4. Avoid btrfs.
- Linode provided kernel does not works.
- Reproducible builds & Dockerfile

:::


# Questions

## 

- How Docker runs on OSX or windows?
- If we build image on Macbook air, can we run this image on Windows laptop (i5 processor) or Raspberry pi ?

## Opensource Projects

- [Fedora Silverblue](https://silverblue.fedoraproject.org/)
- [Guix](https://guix.gnu.org/)
- [Nix](https://nixos.org/)

# Thank You!
