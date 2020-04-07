pipeline {
    agent any
    stages {
        stage(Number1){
            steps{
                sh 'chmod +x ./script/*'
                sh './script/ansible.sh'
                sh 'echo "Nodes linked and Docker Swarm Service Enabled"'
            }
        stage(Deploy Docker Stack Service){
            steps{
                sh './script/docker.sh'
                sh 'echo "Stack Service Deployed"'
            }
        }
        stages(Create Development Environment){
            steps{
                sh './script/before_installation.sh'
                sh './script/run.sh'
                sh 'echo "Development environment created"'
            }
        }
    }
}