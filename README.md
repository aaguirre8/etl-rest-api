# etl-rest-api
How to create a ETL service tutorial.
Reference: https://medium.com/plumbersofdatascience/etl-rest-api-using-python-flask-c8171ac925c5


## Setup
1. Create and source conda env
```bash
$ conda env create -f environment.yml
$ conda activate etl-api
```
Note: After env creation, the terminal may need to be restarted for the env to be activated.

2. Use the Makefile to upgrade pip and to install the dependencies from the requirements.txt file
```bash
$ make install
```

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