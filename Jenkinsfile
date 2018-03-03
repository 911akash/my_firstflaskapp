pipeline {
  agent any
  stages {
    stage('build') {
      parallel {
        stage('build') {
          steps {
            sh 'date'
          }
        }
        stage('whoami') {
          steps {
            sh 'whoami'
          }
        }
      }
    }
    stage('test') {
      steps {
        sh 'echo "test stage"'
      }
    }
    stage('') {
      steps {
        sh 'echo "deploy stage"'
      }
    }
  }
}