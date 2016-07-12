# enav-alpha

GOV.UK UKTI ENav application.

## Features of this application

 - To be added??

## First-time setup

Languages/applications needed
- Python 3.5
- Postgres [postgres](https://www.postgresql.org)
- Heroku Toolbelt [heroku](https://toolbelt.heroku.com)

The app runs within a virtual environment. To [install virtualenv](https://virtualenv.readthedocs.org/en/latest/installation.html), run
```shell
    [sudo] pip install virtualenv
```

Install virtualenvwrapper
```shell
    [sudo] pip install virtualenvwrapper
```

Create a local environment.sh file containing the following:
```shell
echo "
export DATABASE_URL='postgres://@localhost/enav'
"> environment.sh
```

Make a virtual environment for this app:
```shell
    mkvirtualenv -p /usr/local/bin/python3.5 enav-alpha
```

Install dependencies
```shell
    ./scripts/bootstrap.sh
```

## Running the application

Running with django runserver:
```shell
    workon enav-alpha
    python manage.py runserver
```
Then visit [localhost:8000](http://localhost:8000)

Or through heroku:
```shell
    workon enav-alpha
    heroku local
```
Then visit [localhost:5000](http://localhost:5000)

## Running tests

Tests include a pep8 style check, django test script and coverage report.

```shell
    workon enav-alpha
    ./scripts/run_tests.sh
```
