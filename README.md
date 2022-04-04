# valotaku_dev
This repo is for developing valotaku web application.

## Set Up
**Create environment using Docker**
`docker-compose up -d --build`

**Migrate**
`docker-compose exec web python manage.py migrate --noinput`

## Check
http://localhost:8000/
