FROM 3.10.5-alpine3.16

RUN mkdir /api
COPY . /api
WORKDIR /api

RUN apt update
RUN apt install python3-pip -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

