pipeline {
    agent { label 'agent' }

    environment {
        IMAGE_NAME = "hardikdocker18/banking-batch"
        IMAGE_TAG  = "latest"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                  docker build -t $IMAGE_NAME:$IMAGE_TAG .
                '''
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS')]) {

                    sh '''
                      echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                      docker push $IMAGE_NAME:$IMAGE_TAG
                    '''
                }
            }
        }

        stage('Deploy to AWS Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'k8s-config', variable: 'KUBECONFIG')]) {
                    sh '''
                      kubectl delete job banking-batch-job --ignore-not-found
                      kubectl apply -f k8/banking-batch-job.yaml
                      kubectl get pods
                    '''
                }
            }
        }
    }

    post {
        success {
            echo "✅ Banking batch job deployed successfully to AWS Kubernetes!"
        }
        failure {
            echo "❌ Pipeline failed. Check logs."
        }
    }
}

