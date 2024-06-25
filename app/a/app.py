import requests
from flask import Flask
import consul

app = Flask(__name__)
consul_client = consul.Consul()


@app.route('/')
def hello():
    # Get Service B address from Consul
    _, service_b_address = consul_client.catalog.service('service-b')[1][0]

    # Make request to Service B
    response = requests.get(f'https://{service_b_address}:8081/name')
    name = response.text

    return f"Hello, {name}!"


if __name__ == '__main__':
    app.run()
