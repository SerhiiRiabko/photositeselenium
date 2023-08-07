# sudo apt install snap
# sudo snap install docker
# docker - show command
# docker ps -a
# sudo chmode 666 /var/run/docker
# docker images - show images, download from dockerhub
# docker pull postgres - download
# docker ps -a - show active container
# docker run --name bohdan_postgresss + id of images
# docker rm + container_id
# docker stop + id - make innactive
# docker stop $(docker ps -a -q)  - $(docker ps -a -q) - all containers id shows
# docker start +Id
# docker exec -it id /bin/bash
# docker cp Ryanair.pdf id_container:/Ryanair.pdf - copy to container
# docker rmi image_id
#