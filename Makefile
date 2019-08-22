build:
	docker-compose down
	docker-compose build dev

dev: build
	docker-compose run --rm -p 9301:8080 dev sh

test: build
	docker-compose run --rm dev sh ./bin/run-tests.sh