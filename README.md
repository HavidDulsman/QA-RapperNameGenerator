# Rapper Name Generator: Discover your Rapper alter ego!


This project was created in reference to the 'QA Learning Academy Practical SFIA Project' brief This Project meets all of the specifications of said documents and fully displays the ability of the creator.

This Project is due Week 8 of the QA Consultancy DevOps 17th February 2020 Intake.

## Table of Contents

1. [Brief](https://github.com/HavidDulsman/RapperNameGenerator#brief)
    + [Requirements](https://github.com/HavidDulsman/RapperNameGenerator#requirements)
2. [Project Plan](https://github.com/HavidDulsman/RapperNameGenerator#project-plan)
    + [Kanban Board](https://github.com/HavidDulsman/RapperNameGenerator#kanban-board)
    + [Feature Branch Model](https://github.com/HavidDulsman/RapperNameGenerator#feature-branch-model)
3. [Architecture](https://github.com/HavidDulsman/RapperNameGenerator#architecture)
    + [Entity Relationship Diagram](https://github.com/HavidDulsman/RapperNameGenerator#entity-relationship-diagram)
    + [Service Architecture Diagram](https://github.com/HavidDulsman/RapperNameGenerator#service-architecture-diagram)
    + [System Security](https://github.com/HavidDulsman/RapperNameGenerator#system-security)
4. [Risk Assessment](https://github.com/HavidDulsman/RapperNameGenerator#risk-assessment)
    + [Pre/Early Development](https://github.com/HavidDulsman/RapperNameGenerator#preearly-developement)
    + [After Project Completition](https://github.com/HavidDulsman/RapperNameGenerator#after-project-completition)
5. [Deployment](https://github.com/HavidDulsman/RapperNameGenerator#deployment)
    + [List of techonologies used](https://github.com/HavidDulsman/RapperNameGenerator#list-of-used-technologies-and-languages)
6. [Testing](https://github.com/HavidDulsman/RapperNameGenerator#testing)
    + [Pytest report](https://github.com/HavidDulsman/RapperNameGenerator#pytest-functionality)
    + [Coverage report](https://github.com/HavidDulsman/RapperNameGenerator#coverage-report)
7. [Comparisons](https://github.com/HavidDulsman/RapperNameGenerator#comparisons)
    + [Initial Design](https://github.com/HavidDulsman/RapperNameGenerator#initial-design)
    + [Previous Project](https://github.com/HavidDulsman/RapperNameGenerator#previous-project)
8. [Project retrospective](https://github.com/HavidDulsman/RapperNameGenerator#project-retrospective)
    + [Notable Achievements](https://github.com/HavidDulsman/RapperNameGenerator#notable-achievements)
    + [Project Shortcomings](https://github.com/HavidDulsman/RapperNameGenerator#project-shortcomings)
    + [Future Improvements](https://github.com/HavidDulsman/RapperNameGenerator#future-improvements)
9. [Installation Guide](https://github.com/HavidDulsman/RapperNameGenerator#installation-guide)

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
For Sprint 1, we have first created suitable user stories to achieve the minimal viable product, as well as other things i would like to achieve personally. I mainly focused on starting the documentation and planning of the application, whilst using my experience with past projects to design tasks for the first service.
![Sprint 1](https://i.imgur.com/rZqK3tv.png)
#### Sprint 2:
Sprint 2 sees alot of the early design and documentation work being done, as well as alot of the easy tasks. I have opted to implement SQL at the very start of the project, as i believe i have good experience using databases and its inclusion from the start will be beneficial. Tasks for the other services where also made as development for service 1 continued.
![Sprint 2](https://i.imgur.com/EVWX4AT.png)
#### Sprint 3:
At this point we have the application running in some form via the soon-to-be manager node's address. During this stage i look to fully intergrate SQL now, as well as plan for the use of docker for the first time. Future tasks where added for jenkins but these wont be completed for sometime.
![Sprint 3](https://i.imgur.com/wbuzwte.png)
#### Sprint 4:
We now look to test our new docker swarm and stack features with our new system. These will take some time as Docker is a new tool for me and if i get it correct now, it will hopefully mean less errors will be encounters later on. Whilst i have some extra time with testing docker, i am looking to include NGINX into my project now, which will hopefully be easy to complete and help with the security of my project. We can also look into Ansible, a new tool required for the Minimal Viable Product.
![Sprint 4](https://i.imgur.com/YQSgzkm.png)
#### Sprint 5:
Sprint 5 sees rocky development with ansible, causing this sprint to last abit longer than previous. The first major bug/issue was also encountered during this stage as Ansible had some issues with identifying the keys of the manager node, which we where using. More NGINX testign was done to again ensure all was well, and i took a little bit of time to design the final jenkins related taks. I also changed one of the my own users storeis to 'Won't happen' as i believe i now have little time to mess around further with my project.
![Sprint 5](https://i.imgur.com/FJuSar6.png)
#### Sprint 6:
Sprint 6 saw most of ansible working and testing, with me now moving to connecting it all to a Jenkins CI pipeline and the related tasks to complete that. I also looked at some testing, as this was also part of the Minimal Viable Product.
![Sprint 6](https://i.imgur.com/nj2pZyG.png)
#### Completition:
At this point the Minimal Viable product is completed, with the app passing through jenkins and building each new version thanks to GitHub webhooks. There are still more tasks and user stories to cover, and these will be tackled if there is time after documententing and testing is completed.
![Completition](https://i.imgur.com/vteHLnY.png)
#### Post-Completition Sprint
I have designed some new tasks that will give my project some new CRUD functionality. I believe for an additional sprint after my project completition, this is achieveable in around **2 days**, as i have previous experience with creating functions like this from my previous project. **NOTE: This sprint was not completed and is only made to highlight potential changes after completition**
![Future Sprint](https://i.imgur.com/w6KhgoQ.png)

### Feature Branch Model
Building upon the feedback from my last project, i plan on further utilising the feature branch system by incorporating branchs for each of the services. This not only allows me to effectively develop each service on its own, it also allows me to carefully manage the progression of each service. As there is only one of me developing this app, i might be of great use but allows me to prepare for a real world development environment
![branches](https://i.imgur.com/MAvhgQz.png)
As each of the services are completed, the branches can be discarded. The developer branch however can be kept open however as more development can be made to the project outside of the live site if need be.
![github branches](https://i.imgur.com/yUis66s.png)

## Architecture
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
### UI Design
#### Minimal Viable Product
As mentioned, the minimal required product for this project doesnt require too much fucntionality or style for the app and is suppost to be a test of my back-end management skills. For the first UI design, i have kept it very simple but also easy to read for the user, with results being very clear to the user. I have also opted to include my name and github link as a personal touch.
![MVP diagram](https://i.imgur.com/S8lJqKA.png)
#### End for End Product
This is what the design would be like if all of the possible tasks and users stories are accomplished. Notice two new leaderboards, one for everyone and one for similar names to you. Topical images can also be used but i also quite like the simplistic style for this project.
![End Product](https://i.imgur.com/f0FDF8C.png)

### System Security
A massive focal point of this project was an emphasis on project security with various new tools and methods taught to allow us effectively hide certain information from others. With the introduction of **NGINX**, we are able to develop upstreams that listen for particular ports in use and redirect or hide them from the view of people outside our network. With port 5000 utilised by the front end service **(1)**, we must hide this from the viewing of outside users.

Amongst this, we have also implemented stricter access to firewall rules, espcially with regards to the other ports. In the last project, we enabled all addresses **(0.0.0.0:0)** to have access to our project. This has been tightened, with only the development VMs having access during development.
![nginx config](https://i.imgur.com/zDY8FT6.png)

## Risk Assessment
### Pre/Early Developement
A risk assessment was compiled to look and examine risk related to the project, its requirements and demands. Similar to the previous project, this too can be accessed through the repository or by using [this link](https://github.com/HavidDulsman/RapperNameGenerator/blob/master/documentation/rapper_risk_1.xlsx). 

Many of the same risks appear on this risk assessmentas the last project, but some of the reasonings and values of each have changed due to a change in working environment. A **Risk Assessment Matrix** has been implememnted into both documents.

### After Project Completition 
This version of the risk assessment includes the final review of each item and how it impacted the project if at all. Minor changes may also be included. New items are highlighted in Yellow. Access via [this link](https://github.com/HavidDulsman/RapperNameGenerator/blob/master/documentation/rapper_risk_1_FINAL_COMMENTS.xlsx).

## Deployment

![Deployment pipeline diagram of use softwares](https://i.imgur.com/Bjo41HL.png)

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

## Testing
### Pytest Functionality
Now that i have experience with Pytest, i was able to easily conduct tests of some of the core functions of my project, those being the **URLS of both nodes** to ensure each of them are hosting the application, the **SQL functionality** to prove i have connectivity to my SQL database, **getting responses from each service** and finally **cvs functionality**. the files containing the code for these tests can be accessed using [this link](https://github.com/HavidDulsman/RapperNameGenerator/blob/master/testing/test.py)
#### Code for each test type
![URL test](https://i.imgur.com/g07C6LD.png)
![Response Test](https://i.imgur.com/7Zwr1Iq.png)
![CSV test](https://i.imgur.com/yCKNlrm.png)
![SQL Test](https://i.imgur.com/bYd363u.png)

#### Pytest Report From Jenkins
![Pytest Report](https://i.imgur.com/Ym7gmPG.png)

### Coverage Report
This coverage report was made using a combination of the **Pytest** and **Coverage** tools for Python, and where displayed at the end of a Jenkins Pipeline build report. Alot of time was spent researching methods of improving the coverage from the previous project, even though a wider range of tests where conducted, i was still unable to drastically improve the testing coverage. Moving forward i will have to research new ways to test my project.

![coverage top](https://i.imgur.com/NHzXh0P.png)
![coverage bottom](https://i.imgur.com/Ufb9vHD.png)

#### Coverage HTML template
After consulting with my client after the last project, a new HTML template has been generated for the test. This is available by using [this link](https://github.com/HavidDulsman/RapperNameGenerator/blob/master/testing/htmlcov/index.html)

![html preview](https://i.imgur.com/gyvu4FU.png)

## Comparisons
### Initial Design
#### Project Planning and Development
As you can see from the below image, the project had a very healthy lifecycle with a consistent flow of commits and progression on development, testing and documentation. 
![commits](https://i.imgur.com/XrK1qBK.png)
#### Architecture
As all the entities designed where **must have**, all where included into the final design of the SQL table. Whilst there is only 1 table included, it includes all of the data validation and formatting needed for the app and also allows for possible expansion in the future thanks to clearly defined unique identifiers and easy to read columns.
![table in SQL](https://i.imgur.com/po1QVwl.png)

The project also closely follows its service and swarm model previously mentioned. See below as 3 replicas of each node is generated and distributed amongst 2 nodes. 
![docker service](https://i.imgur.com/FpaoIVT.png)
![docker manager node](https://i.imgur.com/QKBOeiw.png)
![docker worker node](https://i.imgur.com/a4mspcT.png)
#### UI
Compared to the two UI renders done prior, the UI matches the style given for the minimal viable product as styling would not issues any additional marks. very light styling has been done to make text appear centered and/or highlighted to express important information, but otherwise there was little time at the end to focus on something so minor as styling.
![looks](https://i.imgur.com/xbkMEhd.png)
### Previous Project
Compared to my previous project, there are many more backend functions espeically with regards networking and multiple nodes. However due to a much more limited time frame, as well as new working conditions, the current project doesnt have as many fleshed out features as the previous one. Whilst Workout accomplished full CRUD functionality, Rapper Name Generator accomplished on Create and Read. 

One could make the arguement that both still feature impeccably for what they are trying to achieve, with the brief for the newer project being much limited than the other.
![previous project](https://i.imgur.com/vBuoaQw.png)

for information on my previous project **Workout**, please feel free to [follow this link](https://github.com/HavidDulsman/Workout)
## Project retrospective
### Notable Achievements
### Effective use of Docker Swarm + Stack
I was able to go beyond with Docker and implement a **Swarm Service** for my project, which would allow two or more node to connect with each other sharing containers and services between each other, improving the efficiency of the application. A **Stack Service** also allows me to quickly deploy my application on to any new or old nodes with all of the tools they need to operate.

### NGINX Implementation
With NGINX acting as the **reverse proxy server** for my application, this allows me to hide any exposed ip addresses so they are not visible to the public when pushed up to GitHub. This massively improved the security of my project and was relatively easy to implement.

### Automation on multiple levels
Automation was a strong point of my previous project, and i was happy to further advance this skill by improving on my use with the same tools with this project. A combination of **GitHub Webhooks** to my Jenkins server allow me to automate new builds of my project whenever it is pushed up to Github. This alongside detailed **Ansible Playbooks** and **Docker-Compose** files allow me implement the latest version of my project quickly and easily on and two machines with little configuration.

### Project Shortcomings
#### Poor project scope
As i had noting during the start of the project, this application would have been lighter with the focus being more on back-end automation and networking. Due to this, i was unable to expand my application in the later stages. I would have like to include some CRUD functionality, as well as some interesting styling and the project might be lacking due to their absense.

#### More poor testing
I went into this project looking to improve the test and coverage of this project compared to the previous, however i was able to only obtain a slight increase of **1%**, making the total 39%. This is quite disappointing, and has encouraged me to research better methods of testing, such as selenium for my 3rd and final project. You can see the full testing report using [this link](https://github.com/HavidDulsman/RapperNameGenerator/blob/master/testing/htmlcov/index.html).

#### Inefficient security
Enchancing the security of my VMs, ports and databases was very important to me during this project. I used my previous experience of database management to store sensitive values and data within the correct host files so that when i pushed this up to local repositories, my personal info wasnt viewable. Whilst i was able to achieve similar results with the local host manager node, the worker node was quite a challenge and thus had to be left out.

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
