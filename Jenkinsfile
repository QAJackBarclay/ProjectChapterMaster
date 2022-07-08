pipeline{
    agent any
    stages{
        stage('App Testing'){
            steps{
                sh "bash test.sh"
            }
        }
        stage('Ansible playbook run'){
            steps{
                sh "ansible-playbook ansible-config/playbook1.yaml"
            }} 
        stage('Building and pushing images'){
            environment{
                DOCKERHUB_USERNAME=credentials('DOCKER_UNAME')
                DOCKERHUB_PASSWORD=credentials('DOCKER_PWORD')
            }
            steps{
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD"
                sh "docker-compose push"
            }
        }
        stage('Run docker compose '){
            steps{
                sh "docker-compose up -d"
            }   
        }
    }
}