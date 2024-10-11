#activate environemtn
scripts/activate

#install django rest
pip install djangorestframework

#create project
django-admin startproject cellphone_store
cd cellphone_store
django-admin startapp store

#run
py manage.py runserver

#make migrations
py manage.py makemigrations

#migrate
py manange.py migrate

#create superuser
py manage.py createsuperuser --username admin --email admin@mail.com




users
admin
admin

test
Password1.0

test2
Password1.0
