@echo off
D:
cd D:\Coding\Homework\Django\geekshop\
python manage.py makemigrations
python manage.py migrate
cmd /k