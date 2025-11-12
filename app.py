"""Example of flask main file."""
import os
from flask import Flask
app = Flask(__name__)


@app.route('/api/hello')
def hello_world():
    """Returns Hello, KubeRocketCI v2 from hostname."""
    hostname = os.getenv('HOSTNAME', 'unknown')
    return f'Hello, KubeRocketCI v2 from {hostname}'


if __name__ == '__main__':
    app.run()
