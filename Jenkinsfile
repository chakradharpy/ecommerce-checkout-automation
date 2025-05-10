pipeline {
    agent any

    environment {
        // Optional: Useful for future environment variables
        // PYTHONPATH is better handled directly in the bat step for Windows
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://your.git.repo.url.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                REM Add workspace to Python path for module imports like 'from pages.home_page import HomePage'
                set PYTHONPATH=%cd%
                
                REM Run pytest and generate HTML + JUnit reports
                pytest --maxfail=5 --disable-warnings --html=report.html --self-contained-html --junitxml=test-results.xml
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
            junit 'test-results.xml'
        }
    }
}
