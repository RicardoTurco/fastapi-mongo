# fastapi-mongo

Simple FastAPI application with MongoDB

## Running

To run application locally:

```
a) Clone this project in your machine


b) To run / up application:

docker compose up -d --build

OBS: 
using a '--build' parameter to not pull the image, because it's not exists.


c) Access documentation/swagger of application:

http://0.0.0.0:8085/docs (on your browser)


d) To access to 'mongo-express':

http://0.0.0.0:8081/ (on your browser)


e) Put credentials:

admin / pass


f) To stop / down application:

CTRL + C
docker compose down
```

## Running (development)

To run application in development time:

```
a) Clone this project in your machine


b) IMPORTANT: Set your version of Python to 3.12.0


c) Run setup command:

- Make setup

OBS:

If not create a virtualenv using the correct version of Python, you can create it manually: 

- poetry env use 3.12
- poetry shell (show the complete path of virtualenv)
- source <path_to_virtualenv>/bin/activate (If name of virtualenv is not in prompt use the command)


d) Install dependencies:

- make install


e) Run ALL tests of application:

- make test

OBS: 

You can also generate the COVERAGE report of tests:

- make test-cov-rep


f) To run / up MongoDB:

- remove the 'fastapi-mongo' service from docker-compose file
- docker compose up -d --build 

OBS: 
using a '--build' parameter to not pull the image, because it's not exists.


g) To run / up application:

- make run


h) Access documentation/swagger of application:

http://0.0.0.0:8085/docs (on your browser)


i) To access to 'mongo-express':

http://0.0.0.0:8081/ (on your browser)


j) Put credentials:

admin / pass


k) To stop / down application:

CTRL + C
docker compose down
```

## Endpoints

The project has the following endpoints:

### - Health Check: application

```
GET /v1/health-check

Returns the health check of 'application'.
```

#### Success (200 - OK):

```
{
  "application": true   # or False
}
```

## Project Structure

Project structure (considering folder start in `fastapi-mongo`):

```

├── fastapi-mongo
│   ├── app
│   │   ├── __init__.py
│   │   ├── database
│   │   │    ├── __init__.py
│   │   │    ├── connection.py
│   │   ├── models
│   │   │    ├── __init__.py
│   │   │    ├── book.py
│   │   ├── repositories
│   │   │    ├── __init__.py
│   │   │    ├── books.py
│   │   ├── routes
│   │   │    ├── __init__.py
│   │   │    ├── v1
│   │   │    │   ├── __init__.py 
│   │   │    │   ├── health_check.py
│   │   ├── schemas
│   │   │    ├── __init__.py
│   │   │    ├── book.py
│   │   ├── services
│   │   │    ├── __init__.py
│   │   │    ├── book_service.py
│   ├── init-scripts
│   │   ├── init.js
│   ├── tests
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   ├── routes
│   │   │    ├── __init__.py
│   │   │    ├── v1
│   │   │    │   ├── __init__.py 
│   │   │    │   ├── test_health_check.py
├── .gitignore
├── .pylintrc
├── config.py
├── docker-compose.yaml
├── Dockerfile
├── env-example
├── LINCESE
├── log_conf.yaml
├── main.py
├── Makefile
├── poetry.lock
├── pyproject.toml
├── README.md
├── urls.py

```

### Main folders

* `fastapi-mongo` - "Main" folder of project.
* `app` - All the RESTfull API implementation is here.
* `app/database` - Contains the classes and methods for connecting to DB.
* `app/models` - Models of project.
* `app/repositories` - Repositories of project.
* `app/routes/v1` - "Routes" module of project (v1 endpoints).
* `app/schemas` - Schemas of project.
* `app/services` - Services of project.
* `init-scripts` - Scripts that running when the docker compose file execute.
* `tests` - All tests of application.

### Files

* `.gitignore` - Lists files and directories which should not be added to git repository.
* `.pylintrc` - Define configurations of pylint.
* `config.py` - Load environment variables from '.env' file.
* `docker-compose.yaml` - Create container from application and DB.
* `Dockerfile` - Create image from application to be used in 'docker-compose' file.
* `env-example` - Template to create '.env' file.
* `LICENSE` - Definitions of licence of application.
* `log_conf.yaml` - Configurations about log messages.
* `main.py` - The Application entrypoint.
* `Makefile` - Make commands available.
* `poetry.lock` - Define specific versions of dependencies.
* `pyproject.toml` - Some configurations of project.
* `README.md` - Instructions and information to run this project locally.
* `urls.py` - Declare all resource routes of project.

## LINTERS

This project has a some LINTERs to mantain the quality of code.

### Pylint

[Pylint](https://www.pylint.org/) check if the code contains errors of syntax and logical.

```
make pylint
```

### Black

Formats the code according to [PEP-8](https://peps.python.org/pep-0008/) standards.

```
black --check . (displays which files need adjustments in code formatting);
black --check --diff <path_to_file> (displays the necessary code formmating changes in a SPECIFIC file - manual adjust);
black . (performs code formatting "automatically" in ALL files);
black <path_to_file> (performs code formatting "automatically" in a SPECIFIC file);
```

### Isort

Performs adjustments in "imports" of project - [ISORT](https://pycqa.github.io/isort/).

```
isort --check . (displays wich files need adjustments in imports);
isort --check --diff <path_to_file> (displays the necessary adjustments in imports in a SPECIFIC file - manual adjust);
isort . (performs adjustments in imports "automatically" in ALL files);
isort <path_to_file> (performs adjustments in imports "automatically" in a SPECIFIC file);
```

### Coverage

To check the COVERAGE of tests of project, is possible execute the follow command:

```
make test-cov
```

To view more details about the COVERAGE, just run the command:

```
make test-cov-rep
```

This will create a folder 'htmlcov' and one file '.coverage' (they should be included in '.gitignore' file). Inside of folder 'htmlcov', just open the 'index.html' file in your browser to view details about the COVERAGE.

To delete the folder and file created, just run command:

```
make clean
```
