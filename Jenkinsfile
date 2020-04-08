pipeline {
    agent any
    stages {
        stage('Set up ansible' ){
            steps{
                sh 'chmod +x ./script/*'
                sh './script/ansible.sh'
                sh 'echo "Nodes linked and Docker Swarm Service Enabled"'
            }
        }
        stage('Set up docker stack service'){
            steps{
                sh './script/docker.sh'
                sh 'echo "Stack Service Deployed"'
            }
        }
        stage('Development environment'){
            steps{
                sh './script/before_installation.sh'
                sh './script/run.sh'
                sh 'echo "Development environment created"'
            }
        }
    }
}