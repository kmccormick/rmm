#!/bin/bash
if [[ -d .git ]] ; then
	git pull
else
	git clone $GIT_REPO .
fi

pip3 install -U -r requirements.txt
chown -R docker:docker /code
exec su - docker -c "python3 /code/django/manage.py runserver"
