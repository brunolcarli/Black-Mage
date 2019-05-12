install:
	pip install -r requirements.txt

run:
	python server/manage.py runserver 0.0.0.0:8000

migrate:
	python server/manage.py makemigrations
	python server/manage.py migrate

shell:
	python server/manage.py shell	
