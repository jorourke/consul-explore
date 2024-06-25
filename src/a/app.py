import logging

import consul
import requests
import uvicorn
from fastapi import FastAPI

app = FastAPI()

consul_client = consul.Consul(
    host="dcx-consul-cluster-dev.consul.79ccb6be-44be-4241-a037-e96e565a87ac.aws.hashicorp.cloud",
    port=443,
    scheme="https"
)
logger = logging.getLogger(__name__)


@app.get('/')
def hello():
    # Get Service B address from Consul
    index, services = consul_client.catalog.service('service-b')
    if services:
        service_b = services[0]
        service_b_address = service_b['ServiceAddress']
        service_b_port = service_b['ServicePort']

        # Make request to Service B
        try:
            response = requests.get(f'http://service-b-service:8081/name')
            name = response.text
        except requests.RequestException as e:
            logger.error(f"Failed request", e)
            raise e
    else:
        name = "Error: Service B not found in Consul"

    return {"message": f"Hello, {name}!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
