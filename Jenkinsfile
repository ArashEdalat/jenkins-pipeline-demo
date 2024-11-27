pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/<your-repo>/jenkins-pipeline-demo.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
            }
        }
        stage('Test') {
            steps {
                echo 'Running Tests...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
