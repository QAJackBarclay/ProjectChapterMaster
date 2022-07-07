# QA-DevOps-Fundamental-Project- MCQ App:  
This repository contains my deliverable for the QA devops fundamental project.


 141  sudo systemctl status nginx
  149  sudo systemctl stop nginx
  245  history | grep system

## Contents:

* [Project Brief](#Project-Brief)  
    Project Chapter Master is the result of my solo project week two for QA ltd, this Project will display my second attempt at building an application, followed by my first attempts at docking, jenkins pipeline and ansible. 

    I kept the application simple in terms of prescence so that I could focus on deployment mainly for this course, with the intention to go back and update or add to the program with rolling updates.
    
* [App Design](#App-Design)
    I designed the app with simplicity in mind as I overcomplicated my first project which left me with unfinished work, so I have scaled the functionality appropriatly to my level at this time. 
    
    <img src=  width="900" height="500"/>

    
* [CI Pipeline](#CI-Pipeline)
    I created the pipeline using a seperate virtual machine for Jenkins to be installed on, then I installed docker on the Jenkins VM to establish a relationship, before troubleshooting until I got my first completed build at build #9. 



* [Risk Assessment](#Risk-Assessment)
    Here I will provide my risk assessment and the projected challenges I can face during this week.

    <img src="https://github.com/QAJackBarclay/ProjectChapterMaster/blob/97c6a3d38f9a2d3e35971dd0e0094ca5737fb211/Images/Risk%20%20Assessment%20Chapter%20Master.PNG " width="900" height="500"/>

* [Testing](#Testing)
    After the successful build of my pipeline, I covered all services to 100% before rebuilding the pipeline to ensure there was no issues in updating.

    Once testing was complete on visual studio code and running through jenkins which took a few build attempts.
    <img src=  width="900" height="500"/>
    
* [The App](#The-App)
    The application has a home html that is visible to the user whilst the backend urls generate the information displayed to the home html.

    The application generates a Chapter of Adeptus Astartes from the sci-fi fantasy tabletop RPG Warhammer 40k. It will then generate given years of service followed by how long it will take before they are deployed to the battlefield.
    
* [Updates](#Updates)
    I would like to add in ranks, weaponry and also a potential database for names and generated information to be stored for a user if they so wished.

* [Docker](#Docker)
    <img src=  width="900" height="500"/>

* [Ansible](#ansible)
    <img src=  width="900" height="500"/>
