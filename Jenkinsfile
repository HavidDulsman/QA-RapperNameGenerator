pipeline {
    agent any
    stages {
        stage(Development Environment){
            steps{
                sh 'chmod +x ./script/*'
                sh './script/before_installation.sh'
                sh './script/run.sh'
                sh 'echo "Development environment created"'
            }
        }
        
    }
}