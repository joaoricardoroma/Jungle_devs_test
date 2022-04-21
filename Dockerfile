# pull official base image
FROM python:3.7.4

# set work directory
#WORKDIR /usr/src/app
WORKDIR /home/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2
RUN apt-get clean && apt-get update
RUN apt-get install -y gcc python3-dev python-dev build-essential default-libmysqlclient-dev musl-dev python-mysqldb

# install dependencies
RUN pip install --upgrade pip --user
COPY requirements.txt /home/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /home/app

EXPOSE 8000
# run entrypoint.prod.sh
RUN python manage.py collectstatic --noinput





