all:
	pip install -r requirements.txt
	docker-compose up -d
	python3 manage.py migrate
	python3 manage.py runserver

test:
	python3 manage.py test

build:
	python3 manage.py makemigrations
	python3 manage.py migrate


