pipeline {
    agent any
    stages {
        stage(Number1){
            steps{
                sh 'chmod +x ./script/*'
                sh './script/ansible.sh'
                sh 'echo "Nodes linked and Docker Swarm Service Enabled"'
            }
        stage(Number2){
            steps{
                sh './script/docker.sh'
                sh 'echo "Stack Service Deployed"'
            }
        }
        stages(Number3){
            steps{
                sh './script/before_installation.sh'
                sh './script/run.sh'
                sh 'echo "Development environment created"'
            }
        }
    }
}