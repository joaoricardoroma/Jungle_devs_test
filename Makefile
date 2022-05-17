all:
	pip install -r requirements.txt
	pip install --upgrade pip
	docker pull postgres:latest
	docker-compose up --build -d
	python3 manage.py migrate
	python3 manage.py runserver

test:
	python3 manage.py test

build:
	python3 manage.py makemigrations
	python3 manage.py migrate

logs:
	docker-compose logs -f --tail 100

