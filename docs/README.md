# ARNEIS documentation

## Run the documentation site in Docker

### Prerequisites

* [Docker Engine](https://www.docker.com/products/container-runtime)

### Build the Docker image

```bash
docker build -t baroloteam/arneis-docs .
```

### Run the Docker container

```bash
docker run -d -p 8000:8000 baroloteam/arneis-docs
```

Verify that the container is up and running

```bash
ps ax | grep baroloteam
```

then open `http://DOCKER_HOST:8000` from your browser.

<!-- EOF -->
