# node 이미지에 파이썬을 설치하는게 더 쉬움 / 파이썬 이미지에 node를 설치하는게 더 귀찮음
FROM node:17.9-alpine3.14

# 패키지 관리자(설치)
#RUN apk add --no-cache python3==3.9.5-r2 py3-pip
RUN apk add --no-cache python3==3.9.16-r0 py3-pip

# 몇가지 의존패키지 설치
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev
RUN apk add --no-cache jpeg-dev zlib-dev

# 링크 생성하기
RUN ln -sf python3 /usr/bin/python

# 작업공간
WORKDIR /code
COPY requirements-dev.txt .
RUN pip install -r requirements-dev.txt

ENTRYPOINT ["ash"]

# 한 컨테이너 안에서 프론트와 백을 같이 구성함.
# 도커에 아직 익숙하지 않으니 우선은 같이 구성해서 학습함.