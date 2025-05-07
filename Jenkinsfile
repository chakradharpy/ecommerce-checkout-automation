
pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning repository...'
                // Git is expected to be configured via Jenkins job
            }
        }

        stage('Set up Python environment') {
            steps {
                echo 'Creating and activating virtual environment...'
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt'
            }
        }

        stage('Run Tests with HTML Report') {
            steps {
                echo 'Running pytest with HTML report...'
                sh '. venv/bin/activate && pytest -v --html=report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
        }
    }
}
