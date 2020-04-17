# test_task_django

How to start this app, run commands listed bellow:

install Docker
navigate to app folder -> src: 
cd some_path/test_task_django/src

use dc.yml file for docker start: 
docker-compose -f dc.yml up -d

make migrations with:
docker exec -it backend_test_task python src/manage.py makemigrations

apply migrations with:
docker exec -it backend_test_task python src/manage.py migrate

load users from fixture with:
docker exec -it backend_test_task python src/manage.py loaddata user.json

collect static files into 'static' folder with:
docker exec -it backend_test_task python src/manage.py collectstatic

