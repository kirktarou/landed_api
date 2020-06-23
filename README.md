# landed_api

`api` — backend application

`build` — build scripts, docker/docker-compose

### Dev environment set-up

Install pyenv and virtualenv:
`brew install pyenv pyenv-virtualenv`

Install python:
`pyenv install 3.8.2`

Create virtualenv:
`pyenv virtualenv 3.8.2 landed_api`

Set local virtualenv:
`pyenv local landed_api`

Install python dependencies:
`cd api && make dev_requirements`

### Start Dev environment
In a separate shell, start the Postgres container:

`cd [project directory] && docker-compose -f build/docker-compose-dev.yml up`

Load the agents from the data file:

`python manage.py load_agents [project directory]/data.json`

Run the server:
`make run`

### Run in API server and Postgres in Docker

Stop dev mode:
Press 'Ctrl-C' in window running the postges Docker container

Run both postges and the django server in Docker containers:
`docker-compose -f build/docker-compose-api.yml up`

Once the server has started, navigate to:
* http://127.0.0.1:8000/doc/ for API documentation
* http://127.0.0.1:8000/api/v1/agents/ to access the agent data
* http://127.0.0.1:8000/api/v1/agents/regions to access the region data
* http://127.0.0.1:8000/api/v1/agents/personas to access the personas data

