# QA-DevOps-Fundamental-Project- MCQ App:  
This repository contains my deliverable for the QA devops fundamental project.


 141  sudo systemctl status nginx
  149  sudo systemctl stop nginx
  245  history | grep system

## Contents:

* [Project Brief](#Project-Brief)  
    Project Chapter Master is the result of my solo project week two for QA ltd, this Project will display my first attempts to create an application, dock, pipeline and ansible in the given timeframe. The applicaiton should be functional and should be correctly deployed.
    
* [App Design](#App-Design)
    I designed the app with simplicity in mind as I overcomplicated my first project which left me with unfinished work, so I have scaled the functionality appropriatly to my level at this time.
    
* [CI Pipeline](#CI-Pipeline)
    I created the pipeline using a seperate virtual machine for Jenkins to be installed on, then I installed docker on the Jenkins VM to establish a relationship, before troubleshooting until I got my first completed build at build #9. 


* [Risk Assessment](#Risk-Assessment)
    Here I will provide my risk assessment and the projected challenges I can face during this week.

    [img] https://github.com/QAJackBarclay/ProjectChapterMaster/blob/97c6a3d38f9a2d3e35971dd0e0094ca5737fb211/Images/Risk%20%20Assessment%20Chapter%20Master.PNG [/img]

* [Testing](#Testing)
    After the successful build of my pipeline, I covered all services to 100% before rebuilding the pipeline to ensure there was no issues in updating.
    

* [The App](#The-App)
    The application has a home html that is visible to the user whilst the backend urls generate the information displayed to the user.
    
* [Updates](#Updates)

* [Known Issues](#Known-Issues)
    nginx, is a pain in my soul.

* [Future Work](#Future-Work)
        stage('deploy'){
            steps{
                #swarmcode " "
            }
        }
        stage('curl'){
            steps{
                #curl " "
            }
        }