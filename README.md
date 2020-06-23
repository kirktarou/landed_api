# landed_api

`api` — backend application

`build` — build scripts, docker/docker-compose

### Development mode

Start the postgres container:

`docker-compose -f build/docker-compose-dev.yml up`

Load the agents from the data file:
`python manage.py load_agents ~[path to]/landed_api/data.json`

Stop dev mode:
Press 'Ctrl-C' in window running the postges docker container

### Run in Docker

Run both postges and the django server in Docker containers:
`docker-compose -f build/docker-compose-api.yml up`

Once the server has started, navigate to:
* http://127.0.0.1:8000/doc/ for API documentation
* http://127.0.0.1:8000/api/v1/agents/ to access the agent data
* http://127.0.0.1:8000/api/v1/agents/regions to access the region data
* http://127.0.0.1:8000/api/v1/agents/personas to access the personas data

