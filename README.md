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
    + [Multi Tier Architecture Diagram]()
4. [Risk Assessment]()

## Brief
As quoted from 'QAC - Practical Project Specification (DevOps):

    " At itscore you are creating an application that generates “Objects” upon a set of 
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
