# Rapper Name Generator: Discover your Rapper alter ego!


This project was created in reference to the 'QA Learning Academy Practical SFIA Project' broef This Project meets all of the specifications of said documents and fully displays the ability of the creator.

This Project is due Week 8 of the QA Consultancy DevOps 17th February 2020 Intake.

## Table of Contents

1. [Brief]()
    + [Requirements]()
2. [Project Plan]()
    + [Kanban Board]()
3. [Architechure]()
    + [Entity Relationship Diagram]()
    + [Use Case Diagram]()
    + [Service Architecture Diagram]()
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
## Architecture
For those have a cheeky look at my repo early, nothing here yet! Will it be big? Maybe. Maybe not.
### Entity Relationship Diagram
One of the requirements for this project was to project the results of Service 4 into a SQl Database. Continuing with the **MoSCoW Method**, only 1 table will feature during my project due to the smaller scope of the project itself. Because of this, the sole table is a **Must Have** part of the project. It will store each item with a unique identifier, as well as VARCHAR columns for the old and new names made for each person
![ERD](https://i.imgur.com/YDgi3RZ.png)
### Use Case Diagram
### Service Architecture Diagram
#### Service 1
#### Service 2 + 3
#### Service 4

## Risk Assessment
### Pre/Early Developement
A risk assessment was compiled to look and examine risk related to the project, its requirements and demands. Similar to the previous project, this too can be accessed through the repository or by using [this link](https://github.com/HavidDulsman/RapperNameGenerator/blob/developer/documentation/rapper_risk_1.xlsx). 

Many of the same risks appear on this 'RA' as the last project, but some of the reasonings and values of each have changed due to a change in working environment.

### After Project Completition 
This version of the risk assessment includes the final review of each item and how it impacted the project if at all. Minor changes may also be included

## Deployment

![Deployment pipeline diagram of use softwares]()

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
### Future Improvements

## Authors
David Hulsman

## Acknowledgements
My Family for supporting me during this training period, as well as Syed for his laidback, but also enjoyable and informative training sessions 
