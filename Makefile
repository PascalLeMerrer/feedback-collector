SHELL := /bin/bash
include .env
export

run: start-db
	cd www && flask --app=__init__.py run

initdb:
	python www/init_db.py

start-db:
	docker run --name db --env POSTGRES_PASSWORD=${DB_PASSWORD} --detach --publish 127.0.0.1:5432:5432 postgres

download-all:
	scp -r breizhcamp-feedback@ssh-breizhcamp-feedback.alwaysdata.net:www .

deploy:
	# https://www.cyberciti.biz/faq/scp-exclude-files-when-using-command-recursively-on-unix-linux/
	rsync -av -e ssh --exclude='env' --exclude='.cache' www breizhcamp-feedback@ssh-breizhcamp-feedback.alwaysdata.net:/home/breizhcamp-feedback/
	@echo -------------------------------------------------------
	@echo Now you must restart the website in the admin interface
	@echo -------------------------------------------------------

psql: 
	docker exec -it db psql -U postgres