pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerHubCredentials')
        DOCKER_IMAGE = "bbamba/bbtlabapp01"  // Update this to your DockerHub image name
        //KUBECONFIG_CONTENT = credentials('kubeconfig')
        //DEPLOYMENT_NAME = "bbtlabapp01"
        //K8S_NAMESPACE = "default"  // Set your namespace
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout code from the Git repository
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh """
                        docker build -t ${DOCKER_IMAGE}:latest .
                    """
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Login to DockerHub and push the image
                    sh """
                        echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                        docker push ${DOCKER_IMAGE}:latest
                    """
                }
            }
        }
    }
}