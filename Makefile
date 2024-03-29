up:
	docker-compose up

down:
	docker-compose down

build:
	docker exec jungle pip install -r requirements.txt
	docker exec jungle python3 manage.py migrate

test:
	docker exec jungle python3 manage.py test

logs:
	docker-compose logs -f --tail 100

run:
	docker exec -it jungle $(command)

attach:
	docker attach jungle

coverage:
	coverage run manage.py test
	coverage report
	coverage html
