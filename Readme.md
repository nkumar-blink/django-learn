## Django

- Every Django Project is a combination of several django applications.
- python web framework
- server side framework
- batteries included
- MVT pattern(Model, View, Template)


### Install Django
- creating a virtual env : ` python -m venv env`
- activating virtual env:  `source env/bin/activate`
- deactivating an env: `deactivate`
- installing django : ` python -m pip install django`
- list all packages listed: `pip3 list`
- start a django project: `django-admin startproject project-name`
- running a django-server:  `python manage.py runserver`
- starting a django app: `python manage.py startapp project`
- migrate command: `python manage.py migrate`
- create superuser: `python manage.py createsuperuser`
- make migrations: ` python manage.py makemigrations`
- list query ran during migration : `python manage.py sqlmigrate modelName migration eg : sqlmigrate store 0001`

## Django concepts
- Dynamic url 
```python
urlpatterns = [
    path('project/<str:pk>/', views.project, name='project')
]
```
- for templates have directory structure like templates/app-name/html file -> so that the html file doesnt clash with other templates (better practise)
- admin panel : simple way to access how our database
- In django we can have 1-1, many to many , and 1-to-many relationship

## Database Queries
- queryset (variable that holds response) = ModelName.objects.all() 
- .object : Model Object Attribute
- .all() : Method(.get(), .filter(), .exclude())