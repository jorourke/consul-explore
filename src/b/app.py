import json
import random

import consul
from src.common.util import setup_logging
from flask import Flask

app = Flask(__name__)
consul_client = consul.Consul(
    host="dcx-consul-cluster-dev.consul.79ccb6be-44be-4241-a037-e96e565a87ac.aws.hashicorp.cloud",
    port=443,
    scheme="https"
)

setup_logging(app)


@app.route('/name')
def get_name():
    # Get names from Consul KV store
    # _, names_data = consul_client.kv.get('names-config/names')
    with open('/app/config/names', 'r') as f:
        names = json.load(f)
        app.logger.debug(f"Names are {names}")

    return random.choice(names)


if __name__ == '__main__':
    app.logger.info(f"Service B is running on port 8081")
    app.run(port=8081, host='0.0.0.0')
