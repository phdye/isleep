pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                sh 'pip install pdm'
                sh 'pdm install'
            }
        }
        stage('Test') {
            steps {
                sh 'pdm run python -m unittest discover tests'
            }
        }
        stage('Package') {
            steps {
                sh 'pdm build'
            }
        }
        stage('Publish') {
            environment {
                TWINE_USERNAME = credentials('pypi-username')
                TWINE_PASSWORD = credentials('pypi-password')
            }
            steps {
                sh 'pip install twine'
                sh 'twine upload dist/*'
            }
        }
    }
}