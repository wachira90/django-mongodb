# django-mongodb
django-mongodb

## install command

```
virtualenv env

pip install django

pip install djangorestframework

django-admin startproject appmain

cd appmain/

python manage.py startapp api

```


```
pip install djongo
pip install pymongo==3.12.1
```

### appmain\appmain\settings.py

```
DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'django',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': 'mongodb://user:pass@host/testdb?authSource=admin&retryWrites=true&w=majority'
            }  
        }
}
```


```
INSTALLED_APPS = [
    'api',
    ...
]
```

## migrate
```
python manage.py makemigrations && python manage.py migrate
```

## runserver

```
python manage.py runserver 0.0.0.0:9000
```

## create adminuser
```
python manage.py createsuperuser --email admin@example.com --username admin
```