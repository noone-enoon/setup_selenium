pipeline {
    agent any

    stages {
        stage('Build image') {
            steps {
                script {
                    docker.build("python-web-tests", "-f Dockerfile .")
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}