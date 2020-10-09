FROM ubuntu:18.04

#ENV FLASK_APP app.webapp
ENV FLASK_DEBUG True
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

#Installation python 3.6
RUN apt update
RUN apt-get install python3-pip wget vim -y
RUN python3 -V
RUN pip3 --version

#Installation mongo shell
RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
RUN echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.2.list
RUN apt install -y gnupg apt-transport-https
RUN apt update -y
RUN apt install -y mongodb-org-shell

#Installation requirements
COPY requirements.txt .
RUN pip3 install -r requirements.txt

VOLUME /var/www
EXPOSE 5000

CMD flask run --host=0.0.0.0
