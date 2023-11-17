run:
	docker-compose up web

debug:
	docker-compose stop web 
	docker-compose rm web
	docker-compose run --rm --service-ports web sh -c "pip install debugpy -t /tmp && python /tmp/debugpy --wait-for-client --listen 0.0.0.0:5678 -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"

build:
	docker-compose build web

bash:
	docker-compose exec web bash

test:
		docker-compose run --rm web sh -c "pytest"

