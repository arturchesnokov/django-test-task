#!/bin/bash

rm /srv/project/run/celery.pid
celery -A test_task worker -l info --workdir=/srv/project/src --pidfile=
