docker run --name authapp-postgres -p 5432:5432 -e POSTGRES_PASSWORD=567234 -d postgres
docker run --name authapp -p 5432:5432 -e POSTGRES_PASSWORD=567234 -d postgres
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
http://127.0.0.1:8000/admin

<!-- python manage.py startapp authapp -->

python manage.py makemigrations
python manage.py migrate
http://localhost:8000/`

User
123456user
