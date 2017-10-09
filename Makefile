# Makefile

VIRTUALENV = venv/

install: create_virtualenv pip_install

create_virtualenv:
	if [ ! -d env ]; then virtualenv -p python3.5 $(VIRTUALENV); fi

pip_install:
	. $(VIRTUALENV)bin/activate; pip3.5 install -r requirements.txt

launch:
	export REDIS_URL="redis://localhost:6379/0"; . $(VIRTUALENV)bin/activate; python3.5 manage.py runserver

test:
	rm -rf __pycache__
	rm -rf tests/__pycache__
	export REDIS_URL="redis://localhost:6379/0"; python3.5 test.py tests
