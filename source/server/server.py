import multiprocessing as mp
import uuid

from flask import request, Flask

from source import config as cfg
from source.back.back import predictor
from source.config import PredictionData

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    uid = str(uuid.uuid4())

    requests.put({
        'data': dict(request.form),
        'id': uid
    })

    predictions[uid] = PredictionData(status=cfg.Status.wait)

    return {
        "success": True,
        "id": uid
    }


@app.route('/test', methods=['POST'])
def test():
    return "OK"


@app.route('/get', methods=['GET'])
def get():
    if ('id' not in request.args) or (request.args['id'] not in predictions):
        return PredictionData(status=cfg.Status.invalid).format()

    res = predictions[request.args['id']]
    if res.status not in [cfg.Status.wait, cfg.Status.process]:
        del predictions[request.args['id']]

    return res.format()


if __name__ == '__main__':
    requests = mp.Queue(cfg.MAX_QUEUE_SIZE)
    predictions = mp.Manager().dict()
    mp.Process(target=predictor, args=(requests, predictions)).start()

    app.run(host="10.0.0.5", port="8080")
