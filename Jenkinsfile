pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                sh 'git clone https://github.com/alejkz/Wog4.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker image build -t My-project .'
                
            }
        }
        stage('Run') {
            steps {
                sh 'docker-compose run -p 8777 --volume=/Scores.txt'
            }
          
        }
     
        stage('Test') {
            steps {
                sh 'python3 e2e.py'
            }
          
        }
       stage('Finalize') {
             steps {
                sh 'docker rm $(docker ps -a -q)'
                sh 'docker push My-project'
            }
          
        }
    }
}
    
