import multiprocessing as mp

from pprint import pprint
from flask import request, Flask

from source import config as cfg
from source.back.back import predictor

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    requests.put(dict(request.form))

    return {
        "success": True
    }


@app.route('/test', methods=['POST'])
def test():
    return "OK"


@app.route('/get', methods=['GET'])
def get():
    return "OK"


@app.route('/check', methods=['GET'])
def check():
    return "OK"


if __name__ == '__main__':
    requests = mp.Queue(cfg.MAX_QUEUE_SIZE)
    predictions = mp.Queue(cfg.MAX_QUEUE_SIZE)
    mp.Process(target=predictor, args=(requests, predictions)).start()

    app.run(host="10.0.0.5", port="8080")
