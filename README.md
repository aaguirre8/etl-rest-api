# python-project-template
This is a template for python projects


## Setup
1. Create and source conda env
```bash
$ conda env create -f environment.yml
$ conda activate env-name
```
Note: After env creation, the terminal may need to be restarted for the env to be activated.

2. Use the Makefile to upgrade pip and to install the dependencies from the requirements.txt file
```bash
$ make install
```

## Scaffold
- repo name
  - app name
    - db
    - module name
      - etl
       - __init_.py
       - readme.md
      - ml
       - __init__.py
       - readme.md
    - shared
    - app.py
  - .env
  - .gitignore
  - environment.yml
  - Makefile
  - README.md
  - requirements.txt
  - setup.py


## Packaging
1. Execute the setup.py script using the following command:
```bash
$ python setup.py bdist_wheel
```

## Postgres Container
The postgres container initialize a virtual db to execute tests in the app isolated from a local env.
To spin the container follow the instructions below:

1. Setup an external volume
```bash
$ docker volume create dbname
```

2. Launch Postgres DB
```bash 
$ docker-compose up -d
```

## Architecture


## Workflow


## TODO


## Existing Issues