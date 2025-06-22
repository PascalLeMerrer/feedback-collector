download-all:
	scp -r breizhcamp-feedback@ssh-breizhcamp-feedback.alwaysdata.net:www .

deploy:
	# https://www.cyberciti.biz/faq/scp-exclude-files-when-using-command-recursively-on-unix-linux/
	rsync -av -e ssh --exclude='env' --exclude='.cache' www breizhcamp-feedback@ssh-breizhcamp-feedback.alwaysdata.net:/home/breizhcamp-feedback/
	@echo -------------------------------------------------------
	@echo Now you must restart the website in the admin interface
	@echo -------------------------------------------------------
