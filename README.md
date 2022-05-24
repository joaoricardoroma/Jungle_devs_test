# Installation

Install Makefile creator on your code reader.

Open your terminal and type:

    Make all

Add those apps to your `INSTALLED_APPS` setting.
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'api',
    'django_filters',
]
```

# API End-Points

- You can now open the API in the Postman and import Collections and Environment from Postman directory

<img src='https://user-images.githubusercontent.com/105290851/169929406-6b3b47a2-7297-4404-abc9-151bb112af41.png'>


    0.0.0.0:8000
    0.0.0.0:8000/api/login
    0.0.0.0:8000/api/sign-up
    0.0.0.0:8000/api/admin/authors
    0.0.0.0:8000/api/admin/articles
    0.0.0.0:8000/api/articles
