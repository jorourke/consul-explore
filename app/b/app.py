import json
import random

import consul
from flask import Flask

app = Flask(__name__)
consul_client = consul.Consul()


@app.route('/name')
def get_name():
    # Get names from Consul KV store
    _, names_data = consul_client.kv.get('names-config/names')
    names = json.loads(names_data['Value'])

    return random.choice(names)


if __name__ == '__main__':
    app.run(port=8081)
