import json
import logging
import random

import consul
import uvicorn
from fastapi import FastAPI

app = FastAPI()
consul_client = consul.Consul(
    host="dcx-consul-cluster-dev.consul.79ccb6be-44be-4241-a037-e96e565a87ac.aws.hashicorp.cloud",
    port=443,
    scheme="https"
)

logger = logging.getLogger(__name__)


@app.get('/name')
def get_name():
    logger.info("Doing get name")
    # Get names from Consul KV store
    # _, names_data = consul_client.kv.get('names-config/names')
    with open('/app/config/names', 'r') as f:
        names = json.load(f)

    return random.choice(names)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
