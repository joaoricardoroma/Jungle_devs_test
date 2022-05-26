### My first Django project
This was my first project using APIs I think I learned a lot and that will help me a lot in future projects in django.
I did these test to test my ability and understand what level I'm on being a test that a junior and a senior would do with the difference in how they would.

# Installation

```python
- Docker
- Docker Compose
- Makefile
```

## To start the project run:

```
make up
```

## To apply your database:

- Rename file app/.env_sample to .env, file already have db connection information
```
make build
```


## To test code run:

```
make test
```

## Articles

    
      "id": "UUID",
      "author": {
        "id": "UUID",
        "name": "Author Name",
        "picture": "https://picture.url"
      },
      "category": "Category",
      "title": "Article title",
      "summary": "This is a summary of the article",
      "firstParagraph": "This is the first paragraph of this article"
      "body": "The book" 

## Authors

    {
    "id": "UUID  ",
    "name": "Author Name",
    "picture": "https://picture.url"}

## Paths

    0.0.0.0:8000 (default page)
    0.0.0.0:8000/api/sign-up (Create an user)
    0.0.0.0:8000/api/login (Get your acess Token)
    0.0.0.0:8000/api/login/refresh (Get your acess Token)
    0.0.0.0:8000/api/admin/authors  (List all authors)  *need token
    0.0.0.0:8000/api/admin/articles (List all articles) * need token
    0.0.0.0:8000/api/articles (list all articles) **can read without token, but not with full access
    
    
# Source

[Jungle Devs - Django Challenge #001] (https://github.com/JungleDevs/django-challenge-001)

# Postman

Import collections

https://github.com/joaoricardoroma/Jungle_devs_teste1/tree/main/postman
