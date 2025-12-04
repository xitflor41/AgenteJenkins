pipeline {
    agent {
        label 'python'
    }

    stages {
        stage('Entorno') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
                sh 'pip install pytest'
                sh 'pip install pandas'
            }
        }

        stage('Descarga'){
            steps{
                git url:'https://github.com/xitflor41/Jenkins-python.git', branch:'main'
            }
        }

        stage('Ejecutar'){
            steps{
                sh 'python3 hola.py'
                sh 'python3 operaciones.py'
            }
        }

        stage('Probar'){
            steps{
                sh 'python -m pytest --junitxml=reports/results.xml'
            }
            post {
                always {
                    junit 'reports/results.xml'
                }
            }
        }
    }
}
