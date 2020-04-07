# Rapper Name Generator: Discover your Rapper alter ego!


This project was created in reference to the 'QA Learning Academy Practical SFIA Project' broef This Project meets all of the specifications of said documents and fully displays the ability of the creator.

This Project is due Week 8 of the QA Consultancy DevOps 17th February 2020 Intake.

## Table of Contents

1. [Brief]()
    + [Requirements]()
2. [Project Plan]()
    + [Kanban Board]()
    + [Feature Branch Model]()
3. [Architechure]()
    + [Entity Relationship Diagram]()
    + [Service Architecture Diagram]()
    + [System Security]()
4. [Risk Assessment]()
    + [Pre/Early Development]()
    + [After Project Completition]()
5. [Deployment]()
    + [List of techonologies used]()
6. [Testing]()
    + [Pytest report]()
    + [Coverage report]()
7. [How to setup]()
8. [Comparison to Initial Design]()
9. [Project retrospective]()
    + [Notable Achievements]()
    + [Project Shortcomings]()
    + [Future Improvements]()
10. [Installation Guide]()

## Brief
As quoted from 'QAC - Practical Project Specification (DevOps):

    " At its core you are creating an application that generates “Objects” upon a set of 
    predefined rules.  These “Objects” can be from whatever domain you wish. "
### Requirements
Some of the requirements for a 'Minimal Viable Product' included:
 + Create a micro-service orientated architecture for a application:
    * Service 1: Used to render Jinja2 templates for interaction, connect to the other services, and finally persisting 
          some data into a SQL Database
    * Service 2/3: Used to generate 'Objects'
    * Service 4: Used to create an 'Object' based of the results of Services 2 and 3 using interesting logic
 + 2 Different implementations between Services 2, 3 and 4
 + Deployment using containerisation and a orchestration tool
 + Advanced CI practices using Jenkins and Ansible
 + Refined skills of services and tools used in the previous project

## Project Plan
### Kanban Board
Once again, my project will utilise a kanban board to affectly produce a task backlog based of the User Stories and the requirements for a Minimal Viable Product. The lay out stay the same, moving from left to right.

The Project will also make use of the MoSCoW Prioritisation method to categorise the importance of tasks and features.
#### Sprint 1:
sprint 1 stuff
![Sprint 1](https://i.imgur.com/rZqK3tv.png)
#### Sprint 2:
![Sprint 2](https://i.imgur.com/EVWX4AT.png)
#### Sprint 3:
![Sprint 3](https://i.imgur.com/wbuzwte.png)
#### Sprint 4:
![Sprint 4](https://i.imgur.com/YQSgzkm.png)
#### Sprint 5:
#### Completition:
#### Future Sprint
![Future Sprint]()
### Feature Branch Model
Building upon the feedback from my last project, i will be further utilising the feature branch system by incorporating branchs for each of the services. This not only allows me to effectively develop each service on its own, it also allows me to carefully manage the progression of each service. As there is only one of me developing this app, i might be of great use but allows me to prepare for a real world development environment
![branches](https://i.imgur.com/MAvhgQz.png)
As each of the services are completed, the branches can be discarded. The developer branch however can be kept open however as more development can be made to the project outside of the live site if need be.

## Architecture
For those have a cheeky look at my repo early, nothing here yet! Will it be big? Maybe. Maybe not.
### Entity Relationship Diagram
One of the requirements for this project was to project the results of Service 4 into a SQl Database. Continuing with the **MoSCoW Method**, only 1 table will feature during my project due to the smaller scope of the project itself. Because of this, the sole table is a **Must Have** part of the project. It will store each item with a unique identifier, as well as VARCHAR columns for the old and new names made for each person
![ERD](https://i.imgur.com/YDgi3RZ.png)
### Service Architecture Diagram
![Overall Diagram](https://i.imgur.com/GWoEZnq.png)
#### Service 1
Service 1, otherwise know as the **front-end** is responsible for everything the user sees. Many of the tools used in the past project can be seen here, from HTML, Jinja2 and Flask. This will be used to display the results made in other services. My app will only start the service once a form has been submitted in the form of the users name. Also the SQL database isnt stored at this service, but does directly interact with service 1.
![S1](https://i.imgur.com/Nil4icp.png)
#### Service 2 and 3
Once input has been made, Services 2 and 3 will be contacted. These are pretty much identical as they both consist of Flask applications that store nothing but lists of words that can be put together to make a result.
![S23](https://i.imgur.com/i8aNV94.png)
#### Service 4
Service 4 will take the results of Service 2 and 3 and merge them together creating a unique result! this result is then referenced in Service 1 where it can be displayed for the user to see!
![S4](https://i.imgur.com/fIubh2M.png)
### System Security
A massive focal point of this project was an emphasis on project security with various new tools and methods taught to allow us effectively hide certain information from others. With the introduction of **NGINX**, we are able to develop upstreams that listen for particular ports in use and redirect or hide them from the view of people outside our network. With port 5000 utilised by the front end service **(1)**, we must hide this from the viewing of outside users.

Amongst this, we have also implemented stricter access to firewall rules, espcially with regards to the other ports. In the last project, we enabled all addresses **(0.0.0.0:0)** to have access to our project. This has been tightened, with only the development VMs having access during development.
![nginx config](https://i.imgur.com/zDY8FT6.png)

## Risk Assessment
### Pre/Early Developement
A risk assessment was compiled to look and examine risk related to the project, its requirements and demands. Similar to the previous project, this too can be accessed through the repository or by using [this link](https://github.com/HavidDulsman/RapperNameGenerator/blob/developer/documentation/rapper_risk_1.xlsx). 

Many of the same risks appear on this 'RA' as the last project, but some of the reasonings and values of each have changed due to a change in working environment.

### After Project Completition 
This version of the risk assessment includes the final review of each item and how it impacted the project if at all. Minor changes may also be included. New items are highlighted in Yellow. Access via [this link](https://github.com/HavidDulsman/RapperNameGenerator/blob/developer/documentation/rapper_risk_1_FINAL_COMMENTS.xlsx).

## Deployment

![Deployment pipeline diagram of use softwares](https://i.imgur.com/jYTQLgI.png)

### List of used technologies and languages
* **GitHub:** Version Control System*
* **Jenkins:** Continuous Intergration Server*
* **Google Cloud Services:** Live Environment + SQL Database Host*
* **Visual Studio Code:** IDE for frontend and backend development. Used the following languages:
    - **Python 3:** Logic and Functionality*
    - **HTML:** Front-end GUI design*
    - **CSS:** Styling and design of front-end GUI*
    - **Flask:** Connects front-end and back-end*
    - **Jinja2:** Pass variables between Python and HTML*
    - **MySQL:** Allows for access of SQL Databases, as well as query-based functions*
* **Trello:** Kanban board and Project tracking*
* **Docker:** Containerisation
* **Docker Swarm + Stack:**  Orchestration
* **Dockerhub:** Version Control for Docker Images and Containers
* **Ansible:** Configuration Management
* **NGINX:** Load Balancing

*: Technologies and tools also used in the first project

## How to Setup

## Comparisons to Original Design

## Project retrospective
### Notable Achievements
### Project Shortcomings
#### Poor project scope
As i had noting during the start of the project, this application would have been lighter with the focus being more on back-end automation and networking. Due to this, i was unable to expand my application in the later stages. I would have like to include some CRUD functionality, as well as some interesting styling and the project might be lacking due to their absense.

#### 
### Future Improvements
#### More use of nodes
The project challenged me to make use of multiple nodes and addresses to balance the load and learn distributing traffic as well as the security behind all of these methods. Whilst i had demonstrated this with a **Manager** and **Worker** node each, i would have hoped to use more nodes to further demonstrate this way of thinking. 

#### CRUD Implementation
If i had known earlier, I would have tried to implement more CRUD functionality into my works, but the current scope of my work didnt really allow me to full expand into these ideas.

#### Selenium testing
Yet again, i felt like the test portion of my project was lacking. I felt this time i might have been the simplicity of my project that might have been the reasoning. Selenium has been mentioned a couple of times since starting and i feel like if i learn how to use and implement it, it could have a massive impact into how i test the project.

## Installation Guide

## Authors
David Hulsman

## Acknowledgements
My Family for supporting me during this training period, as well as Syed for his laidback, but also enjoyable and informative training sessions 
