pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerHubCredentials')
        DOCKER_IMAGE = "bbamba/bbtlabapp01"  // Update this to your DockerHub image name
        KUBECONFIG_CONTENT = credentials('kubeconfig')
        DEPLOYMENT_NAME = "bbtlabapp0-deployment"
        K8S_NAMESPACE = "bbthomelab"  // Set your namespace
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

        stage('Setup Kubernetes Config') {
            steps {
                script {
                    // Set up kubeconfig
                    sh """
                        mkdir -p ~/.kube
                        echo "$KUBECONFIG_CONTENT" > ~/.kube/config
                    """
                }
            }
        }

         stage('Deploy to Kubernetes') {
            steps {
                script {
                         // Apply the deployment YAML to the Kubernetes cluster
                    sh 'kubectl apply -f /home/bbtadmin/myDeployments/bbtlabapp01/deployment.yml --namespace=${K8S_NAMESPACE}'

                    // Check the rollout status of the deployment
                    sh "kubectl rollout status deployment/${DEPLOYMENT_NAME} --namespace=${K8S_NAMESPACE}"
                }
            }
        }

        post {
          always {
            // Clean up Docker images after the build
            sh "docker rmi ${DOCKER_IMAGE}:latest || true"
          }

          success {
            echo "Deployment successful!"
          }

          failure {
            echo "Deployment failed."
          }
        }
    
    }
}