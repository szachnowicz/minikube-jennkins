pipeline {
    agent any
    parameters {
        string(name: 'APP_NAME', defaultValue: 'python', description: 'Name of the application to build and deploy')
    }
    environment {
        REGISTRY = 'localhost:5000'
    }
    stages {
        stage('Build') {
            steps {
                script {
                    dir("apps/${params.APP_NAME}") {
                        docker.build("${REGISTRY}/${params.APP_NAME}:latest")
                    }
                }
            }
        }
        stage('Push to Registry') {
            steps {
                script {
                    docker.withRegistry('', 'docker-creds') {
                        docker.image("${REGISTRY}/${params.APP_NAME}:latest").push()
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    dir("apps/${params.APP_NAME}/k8s") {
                        sh 'kubectl apply -f deployment.yaml'
                        sh 'kubectl apply -f service.yaml'
                    }
                }
            }
        }
    }
}