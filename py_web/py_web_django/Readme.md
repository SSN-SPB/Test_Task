# 1 Initial install
## Set venv
```
python -m venv dvenv
dvenv\Scripts\activate
```

## Install dependencies
```
pip install django
```

## check availability
```
django-admin --version

expected: 5.2.15
```


# 2 Create a Django Project
## Start a new project
```
django-admin startproject config .
```

### Expected file structure
```
myproject/
│
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── venv/
```

## Create an App
```
python manage.py startapp hello
```

### Expected file structure
```
myproject/
│
├── ...
├── hello/
│   └──migrations
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── wsgi.py
│       ├── models.py
│       ├── tests.py
│       └── views.py
└── venv/
```
# 3 Edit files
#### hello/views.py:
```
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
```


#### config/urls.py:
```
from django.contrib import admin
from django.urls import path

from hello.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
```

# 4 Run Database Migrations

Django needs some internal tables:
```
python manage.py migrate

You should see several OK messages.

  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK

```

# 5 Start the Server
```
python manage.py runserver

Output:
...
Django version 5.2.15, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
...
```

## Test the server
Open http://127.0.0.1:8000/
```
Expected output
Webpage with "Hello, Django!" text should be displayed.
```

# 6 Quit
```
Ctrl+C
```
# 7 Restart the server
```
python manage.py runserver
```