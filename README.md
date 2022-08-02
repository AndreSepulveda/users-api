### Introduction

This is a simple implementation to manage users for a web application using FastAPI.

I've seen PyCharm's FastAPI tutorial and I'm trying to implement something similar by heart, so many things you'll see here are actually going to be pretty much the same.

### Software Installation

- [x] [Docker](https://www.docker.com/) - Docker helps developers bring their ideas to life by conquering the complexity of app development.


- [x] [Kubernetes](https://kubernetes.io/) - also known as K8s, is an 
 open-source system for automating deployment, scaling, and management of containerized applications.


- [x] [Helm](https://helm.sh/) - The package manager for Kubernetes. Helm helps you manage 
Kubernetes applications — Helm Charts help you define, install, and upgrade even the most complex Kubernetes application.


- [x] [PostgreSQL](https://www.postgresql.org/) - The World's Most Advanced Open Source Relational Database


- [x] [Redis](https://redis.io/) - open source (BSD licensed), in-memory data structure store, used as a database, cache, and message broker


## System Dependencies

- Make sure your system is up-to-date.
- Run the below command to install python system 
dependencies along-with postgres driver.

```bash

$ sudo apt-get install libpq-dev python-dev libssl-dev

```



## Python Dependencies

- Installing Python Packages

```bash

$ pip install -r requirements.txt

```

- Running Uvicorn Server

```bash

$ uvicorn main:app --reload

```

## Environment

Make sure to update the environment variables in **UserManagement/config.py**, before starting up the project.

## Celery

Make sure before starting up Celery, redis is up and running.

Command to start celery worker :

```bash
$ celery -A main.celery worker -l info
```
or with execution pool
```bash
$ celery -A main.celery worker -l info --pool=prefork
```

Reference Materials:
* [Celery Execution Pools: What is it all about?](https://www.distributedpython.com/2018/10/26/celery-execution-pool/)
* [A complete guide to production-ready Celery configuration](https://medium.com/koko-networks/a-complete-guide-to-production-ready-celery-configuration-5777780b3166)
* [Eliminating Task Processing Outages by Replacing RabbitMQ with Apache Kafka Without Downtime](https://doordash.engineering/2020/09/03/eliminating-task-processing-outages-with-kafka/)


## Testing

Before proceeding make sure you have created a test database in Postgres.


## Alembic

Command to init a migration:
```bash
$ alembic init alembic
```

to create a new version:

```bash
$ alembic revision --autogenerate -m "migration name"
```

and to upgrade/download version:

```bash
$ alembic upgrade head
```
