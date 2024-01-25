# django-seft-taught-tutorial

# 04:42:00 to 04:35:00 Unit Test

## Set Up:

- mkdir buildDjango
- cd buildDjango
- python3 -m venv tutorial-env

## To activate your vitual environment

- use git bash as your terminal and run the command below
  `source tutorial-env/Scripts/activate `
  [কোন অসুবিধা হলে নতুন টর্মিনাল নিতে হবে]

* `pip3 install django`
* `python -m django --version` [according to tutorial python3 -m django version]

## Project Creation:

- `django-admin startproject chefsTable`
- `cd chefsTable`
- `python manage.py runserver` [for starting the server]

## App creation:

- `python -m startapp myapp`

## Project Level urls.py

- ` urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('littleLemon.urls')),

] `

## App Level urls.py

`
urlpatterns = [
path('menu/',views.menu),
path('menu_card/',views.menu_by_id),
path('input/',views.input_form),
path('tst/',views.test_form)

]
`

## Super User Creation

`python manage.py createsuperuser`

## Regular Expression for URLs

`r’^menu_item/[0-9]{2}/$’`

## Model:

- python manage.py shell
- In any error shows after above command then try below code
- In the projects settings.py file
  `
INSTALLED_APPS = [
 'littleLemon.apps.littleLemonConfig',
]`

- python manage.py makemigrations
- python mange.py migrate
- python manage.py showmigrations

[ It is quite confused that you get this doesn't declare an explicit app_label error. But deleting this __init__.py file solved my problem.]

- from littleLemon.models import Menu
- python manage.py shell

`

> from littleLemon.models import Menu
> Menu.objects.all()
> <QuerySet []>
> m = Menu.objects.create(name = 'pasta', cuisine = 'italian', price = 10)
> n = Menu.objects.create(name = 'taco', cuisine = 'mexican', price = 20)  
> Menu.objects.all()
> <QuerySet [<Menu: Menu object (1)>, <Menu: Menu object (2)>]>
> `

# Django Admin User Ceration

### Tutorial Time 3:18:47 to

- `python .\chefsTable\manage.py createsuperuser`

# MySQL Configuration

- install mysqlclient with command
  `pip install mysqlclient`

`'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'littleLemon',
        'USER': 'root',
        'PASSWORD': '123',
        'HOST':'localhost',
        'PORT':'8080',
         'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }
    }
`
