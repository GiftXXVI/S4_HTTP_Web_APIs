environment vars
docker run --env-file env.list ubuntu

docker run -e MYVAR1 --env MYVAR2=foo --env-file ./env.list ubuntu bash

docker run --env-file=env_file_name alpine env

run interactively
docker run -it -d -p 8080:8080 my_image_name
