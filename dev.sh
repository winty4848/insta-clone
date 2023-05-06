#!/bin/bash
docker network create instaclone
docker run -d -p 9999:5432 -e POSTGRES_DB=service -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=1234 --name instaclone-db --net instaclone postgres
docker build -t instaclone:test .
# 도중에 컨테이너 이름이 이미 있다는 오류가 떠서 삭제해주고 진행했음. docker rm ~~~
# 포트 2개를 개방해서 각각 다른 역할로 사용할거임.
docker run -it -p 9998:8000 -p 9997:3000 -v ${PWD}:/code --name instaclone-01 instaclone:test