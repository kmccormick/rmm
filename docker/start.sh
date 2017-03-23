#!/bin/bash
if [[ -d .git ]] ; then
	git pull
else
	git clone $GIT_REPO .
fi

if [[ -r /local_settings.py ]] ; then
	ln -sf /local_settings.py /code/rmm/local_settings.py
fi

pip3 install -U -r requirements.txt
chown -R docker:docker /code
echo "Starting server..." >&2
exec su - docker -c "python3 /code/django/manage.py runserver 0.0.0.0:8000"
