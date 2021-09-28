# Overview
![Deploy](https://github.com/Mutestock/mini-project-loner-edition/actions/workflows/deploy.yml/badge.svg)

Project by cph-hw98 & cph-sn311.

Since all of these technologies should be relatively universal and interoperable, we'll be making this assignment in various different languages and frameworks as an exercise 


- REST: Typescript (deno) 
- SOAP: C# (ASP.NET Core)
- gRPC: Rust (tonic) 
- Migration: Python
- Frontend: Typescript (Angular)

An additionally container running Python will be doing the database migration.

The assignment definition can be seen in [mini-project-loner-edition/A3-MP-API.pdf](https://github.com/Mutestock/mini-project-loner-edition/blob/master/A3-MP-API.pdf)

# Installation

1. Clone the repo by running: `git clone https://github.com/Mutestock/mini-project-loner-edition.git`
2. `cd ./mini-project-loner-edition`
3. Then run (requires docker & docker-compose): `docker-compose up`

**NOTE: Web application is running on** http://localhost:33333 **locally.**

Be advised that pulling the containers and compiling their contents will take some time.

# Deployment 
**NOTE: The deployment of the frontend currently has some issues displaying students (grpc) & teachers (soap). It's possible to to call the endpoints directly on their port with a tool like** [BloomRPC](https://github.com/uw-labs/bloomrpc) **&** [Wizdler](https://chrome.google.com/webstore/detail/wizdler/oebpmncolmhiapingjaagmapififiakb?hl=en)**.**

The solution is deployed at:
## Frontend:
  http://159.65.54.148/

## Backend:
- REST - http://159.65.54.148:10020/grade
- gRPC - http://159.65.54.148:10030 (.proto file are located at [mini-project-loner-edition/grpc/proto/student/student.proto](https://github.com/Mutestock/mini-project-loner-edition/tree/master/grpc/proto/student))
- SOAP - http://159.65.54.148:10040/Service.svc

# Techstack
### Backend
- C# - SOAP
- Rust - gRPC
- Python - migration(Database population and initialization)
- Typescript(Deno) - REST

### Databases
- PostgreSQL

### Frontend
- Angular

### DevOps
- Github Actions, DigitalOcean

### Utilities
- GitHub

# Reasoning

There are multiple reasons why we've decided to solve the assignment like this

1.  The education we're currently taking involves a lot of copying and pasting. We believe this is counterintuitive. We need to make our own solutions for the sake of learning.
2. Being able to use multiple tools and languages makes us more versatile as programmers.
3. Using multiple and completely different languages in the context of SOAP, REST and gRPC and being able to use them together cooperatively on the same platform (frontend Angular), 
    showcases the interoperability and independance of the technologies.
4. Creating the services like this allows us to easily reuse and expand them for future projects.

## Envoy proxy
Envoy is required because our frontend is communicating directly with a gRPC server over gRPC-web. There are some message transportation errors since gRPC-web [uses http/2](https://grpc.io/blog/state-of-grpc-web/).


# Ports
- Web Application: 80 or 33333
- Postgres DB: 10010
- REST service: 10020
- gRPC service: 10030
- SOAP service: 10040
- Envoy Proxy: 10050
- Soap to rest translater service: 10060

# Diagrams
Note that:
- REST is responsibile for Grades and relations
- gRPC is responsible for Student
- SOAP is responsible for Teachers

![alt text](/resources/er_diagram.png "er_diagram")
