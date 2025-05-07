pipeline {
  agent any

  environment {
    PIP_INDEX_URL = "https://pypi.org/simple"  // Or use a fast mirror like https://mirrors.aliyun.com/pypi/simple/
    PIP_TIMEOUT = "120"
    PIP_RETRIES = "5"
  }

  stages {
    stage('Install Python Dependencies') {
      steps {
        retry(3) {
          sh '''
            python3 -m venv venv
            source venv/bin/activate
            pip install --upgrade pip
            pip install -r requirements.txt \
              --default-timeout=$PIP_TIMEOUT \
              --retries=$PIP_RETRIES \
              -i $PIP_INDEX_URL
          '''
        }
      }
    }
  }
}
