pipeline{
    agent any
    stages{
        stage('App Testing'){
            steps{
                sh "bash test.sh"
            }
        }
        stage('Building and pushing images'){
            environment{
                DOCKERHUB_USERNAME=credentials('DOCKER_UNAME')
                DOCKERHUB_PASSWORD=credentials('DOCKER_PWORD')
            }
        }
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
            steps{
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD"
                sh "docker-compose push"
            }
        }
    }
}