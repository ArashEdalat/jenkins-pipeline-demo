# Install the docker file
sudo apt-get update
sudo apt-get install -y docker.io

# Run Jenkins in docker image
docker pull jenkins/jenkins:lts
docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts

# Access Jenkins UI
docker exec <container_id> cat /var/jenkins_home/secrets/initialAdminPassword