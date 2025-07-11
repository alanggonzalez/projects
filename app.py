from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import logging

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Setup logging
logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route('/')
def hello():
    app.logger.info("Hello endpoint was reached")
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
