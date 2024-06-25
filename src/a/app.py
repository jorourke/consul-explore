import consul
import requests
from flask import Flask

from src.common.util import setup_logging

app = Flask(__name__)
consul_client = consul.Consul(
    host="dcx-consul-cluster-dev.consul.79ccb6be-44be-4241-a037-e96e565a87ac.aws.hashicorp.cloud",
    port=443,
    scheme="https"
)

setup_logging(app)


@app.route('/')
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
            app.logger.error(f"Error connecting to Service B: {e}")
            raise e
    else:
        name = "Error: Service B not found in Consul"

    return f"Hello, {name}!"


if __name__ == '__main__':
    print(f"Service A is running on port 8080")
    details = consul_client.catalog.service('service-b')
    print(f"details: {details}")
    app.run(debug=True, port=8080, host='0.0.0.0')
