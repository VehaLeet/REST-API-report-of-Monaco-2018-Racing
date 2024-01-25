# REST API report of Monaco 2018 Racing

## Introduction
This application convert data from files to database, and display info about racers.

## Features
- Can convert ".log", and ".txt" files to database.
- Can display info using API endpoints.

## Getting Started
* For convert files use: "py converter.py --files [DATA DIRECTORY] --db drivers"
* For start server use: "flask --app main run"
* For display info about racing report use:"http://localhost:5000/api/v1/report/"
* For display info about racer use racer's abbreviation:"http://localhost:5000/api/v1/report/svf"

additionally you can change display method,
like XML representation, using url query:
"http://localhost:5000/api/v1/report/?format=xml"

### Prerequisites

* [Flask](https://flask.palletsprojects.com/en/3.0.x/installation/)~=2.2.2
* [peewee](https://docs.peewee-orm.com/en/latest/peewee/quickstart.html)~=3.17.0
* [pytest](https://docs.pytest.org/en/7.1.x/getting-started.html)~=7.2.0
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)~=4.11.1
* [flasgger](https://github.com/flasgger/flasgger)~=0.9.5

