docker run --rm --network network-postgres \
    -e SONAR_HOST_URL="http://sonarqube:9000" \
    -e SONAR_SCANNER_OPTS="\
    -Dsonar.projectKey=DemoPython2 \
    -Dsonar.sources=. \
    -Dsonar.python.version=3.14 \
    -Dsonar.scm.provider=git \
    -Dsonar.scm.disabled=false" \
    -e SONAR_TOKEN="sqp_9706d72a4fc0c880ef7706864cc3a7e91fbe5f5b" \
    -v "/Users/ederlino.tavares/dev/projects/bca/python-demo:/usr/src" \
    -v "/Users/ederlino.tavares/dev/projects/bca/python-demo/.git:/usr/src/.git" \
    --platform='linux/amd64' \
    sonarsource/sonar-scanner-cli
