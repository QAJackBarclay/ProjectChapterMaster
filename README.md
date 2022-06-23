##
#FROM python:3.8

#WORKDIR /app

#COPY . .
#ADD . . can retrieve past local such as URL over COPY

#ENV foo=bar
#RUN pip3 install flask
#EXPOSE 5000

#ENTRYPOINT ["python3", "app.py"]
#CMD ["python3", "app.py"]  if both, there will be arguements but does same things.


#If secret key or database uri do not declare in dockerfile because it'll be on a repository for everyone to see.

#AMAZING CODE
##docker stop $(docker ps -q) && docker rm $(docker ps -aq)

#export MYSQL_ROOT_PASSWORD=password123
#docker run -d --env MYSQL_ROOT_PASSWORD= --name Project_Chapter_Master --network Project_Chapter_Master
#docker network inspect # ProjectChapterMaster
