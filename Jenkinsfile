pipeline {
    agent any

    environment {
        // Set PYTHONPATH so relative imports like "from pages import ..." work
        PYTHONPATH = "${env.WORKSPACE}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://your.git.repo/url.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest and generate both HTML and JUnit reports
                bat 'pytest --maxfail=5 --disable-warnings --html=report.html --self-contained-html --junitxml=test-results.xml'
            }
        }
    }

    post {
        always {
            // Archive the HTML report for download
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true

            // Enable Jenkins to parse test results for pass/fail trends
            junit 'test-results.xml'
        }
    }
}
