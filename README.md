# test_task_django

How to start this app:

install Docker
navigate to app folder -> src: #cd some_path/test_task_django/src
use dc.yml file for docker start: #docker-compose -f dc.yml up -d

navigate to backend container: #docker exec -it backend_test_task bash

in backend , from 'src' folder run:
python manage.py makemigrations
python manage.py migrate

python manage.py loaddata user.json

