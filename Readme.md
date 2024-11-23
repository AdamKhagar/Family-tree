# Family tree

## Quickstart

1. Download Python 3.12.4 . I recommend using `pyenv` for it.
2. `poetry shell && poetry install`
3. Define env files `.envs/.django`, `.envs/.postgres`. Examples are provided.
4. `docker-compose -f docker-compose.yml up --build`
5. `cd app && python manage.py migrate`
6. `python manage.py runserver`

### Optional steps

7. You can fill the database with data by running `python manage.py fill --families 10 --depth 7` which will create 10 families with 7 generations. In each generation will be created a few siblings
8. Also you can use admin page, but for that you are going to need superuser `python manage.py createsuperuser`

## API

1. GET v1/people
2. GET v1/people/<int>
3. GET v1/people/<int>/ancestors/?depth=<int>
4. POST v1/people
5. PUT v1/people/<int>
6. PATCH v1/people/<int>
7. DELETE v1/people/<int>

