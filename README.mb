# Crawler Benefits API 1.0.0 

The proposed structure is described as follows.

```
flask_layout_crawler_benefits/
    app/
    ├── config/
    │   ├── __init__.py
    │   └── config.py
    │
    ├── controller/
    │   ├── __init__.py
    │   ├── benefits_controller.py
    │   └── errors_controller.py
    │
    ├── model/
    │   ├── __init__.py
    │   └── benefits_service.py
    │
    ├── service/
    │   ├── __init__.py
    │   └── crawler_client.py
    │
    ├── static/
    │   ├── __init__.py
    │   ├── swagger.json
    │   └── swagger.yaml  
```

## Prerequisites

* Docker Desktop for Mac and Windows, Docker Compose is included as part of those desktop installs.

* On Linux systems, first install the Docker Engine for your OS as described on the Get Docker page, then come back here for instructions on installing Compose on Linux systems.

## Starting the development environment

### Using Docker
Building the container

```sh
$ docker-compose up --build -d
```

### For Swagger Documentation open link below on browser

Swagger: http://localhost:3000/api/docs

### To run the tests

```sh
$ docker exec -it crawler_benefits_api_dev_app bash
```

```sh
@container $ python -m unittest discover -v
```


