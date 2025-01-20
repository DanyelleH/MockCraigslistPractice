docker-compose up -d --build
sleep 5

docker exec -it assessment-4-api-1 /src/manage.py makemigrations 
docker exec -it assessment-4-api-1 /src/manage.py migrate 

docker exec -it assessment-4-api-1 /src/manage.py loaddata backup.json