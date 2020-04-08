pipeline {
    agent any
    stages {
        stage('Development environment'){
            steps{
                sh 'chmod +x ./script/*'
                sh './script/before_installation.sh'
                sh './script/ansible.sh'
                sh './script/docker.sh'
                sh 'echo "Stack Service Deployed"'
            }
        }
        
    }
}