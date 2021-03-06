# project2-osvaldo-s-children

Example of a basic Django file structure:

    [projectname]/                  <- project root
    ├── [projectname]/              <- Django root
    │   ├── __init__.py
    │   ├── settings/
    │   │   ├── common.py
    │   │   ├── development.py
    │   │   ├── i18n.py
    │   │   ├── __init__.py
    │   │   └── production.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── apps/
    │   └── __init__.py
    ├── configs/
    │   ├── apache2_vhost.sample
    │   └── README
    ├── doc/
    │   ├── Makefile
    │   └── source/
    │       └── *snap*
    ├── manage.py
    ├── README.rst
    ├── run/
    │   ├── media/
    │   │   └── README
    │   ├── README
    │   └── static/
    │       └── README
    ├── static/
    │   └── README
    └── templates/
        ├── base.html
        ├── core
        │   └── login.html
        └── README

Source: https://django-project-skeleton.readthedocs.io/en/latest/structure.html


## What is WSGI
WSGI runs the Python interpreter on web server start, either as part of the web server process (embedded mode) or as a separate process (daemon mode), and loads the script into it. Each request results in a specific function in the script being called, with the request environment passed as arguments to the function.

Source: https://stackoverflow.com/questions/4929626/what-are-wsgi-and-cgi-in-plain-english

## Implementing Google Maps with Django
https://github.com/madisona/django-google-maps