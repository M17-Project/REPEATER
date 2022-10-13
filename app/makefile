runserver:
	DEBUG=1 python manage.py runserver 0.0.0.0:8080
gunicorn:
	DEBUG=1 gunicorn --bind :8080 repeater.wsgi
