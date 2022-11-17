pipeline {
 	agent any
 	stages {
 		stage ('Checkout') {
 			steps {
 				git branch:'main', url: 'https://github.com/suhailii/3103LabTest.git'
 			}
 		}
 
 		stage('Code Quality Check via SonarQube') {
 			steps {
 				script {
 					def scannerHome = tool 'SonarQube';
 						withSonarQubeEnv('SonarQube') {
 						sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=Testing -Dsonar.sources=."
 						}
 					}
 				}
 			}
 		}
 	post {
 		always {
 			recordIssues enabledForFailure: true, tool: sonarQube()
 		}
 	}
}
