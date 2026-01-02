pipeline {
    agent { label 'agent' }

    stages {
        stage('Clone') {
            steps {
                echo "Code pulled"
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t hardikraina/banking-batch .'
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push hardikraina/banking-batch'
            }
        }
    }
}
