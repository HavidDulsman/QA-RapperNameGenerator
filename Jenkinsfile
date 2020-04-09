pipeline {
    agent any
    stages {
        stage('Development environment'){
            steps{
                sh 'chmod +x ./script/*'
                sh './script/installation.sh'
                sh './script/ansible.sh'
                sh './script/docker.sh'
            }
        }
        stage('Testing Environment'){
            steps{
                sh './script/test.sh'
            }
        }
        
    }
}