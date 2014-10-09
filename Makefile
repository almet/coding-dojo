dist:
	landslide config.cfg --copy-theme

upload:
	rsync -e "ssh -p 22" -P -rvz --delete * alexis@172.19.2.119:/home/www/notmyidea.org/cours/cmm/
