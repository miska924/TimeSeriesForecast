import json
import multiprocessing as mp
import uuid

from flask import request, Flask

from source import config as cfg
from source.server import config as server_cfg
from source.back.back import executor
from source.config import PredictionData
from source._helpers import as_enum
from source.server.config import ExecType

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    uid = str(uuid.uuid4())

    print(json.loads(request.get_data(), object_hook=as_enum))

    requests.put({
        'data': json.loads(request.get_data(), object_hook=as_enum),
        'id': uid,
        'type': ExecType.predict
    })

    with results_lock:
        results[uid] = PredictionData(status=cfg.Status.wait)

    return {
        "success": True,
        "id": uid
    }


@app.route('/cross-validate', methods=['POST'])
def cross_validate():
    uid = str(uuid.uuid4())

    print(json.loads(request.get_data(), object_hook=as_enum))

    requests.put({
        'data': json.loads(request.get_data(), object_hook=as_enum),
        'id': uid,
        'type': ExecType.cross_validate
    })

    with results_lock:
        results[uid] = PredictionData(status=cfg.Status.wait)

    return {
        "success": True,
        "id": uid
    }


@app.route('/test', methods=['POST'])
def test():
    return "OK"


@app.route('/get', methods=['GET'])
def get():
    with results_lock:
        if ('id' not in request.args) or (request.args['id'] not in results):
            return PredictionData(status=cfg.Status.invalid).format()

        res = results[request.args['id']]
        if res.status not in [cfg.Status.wait, cfg.Status.process]:
            del results[request.args['id']]

    return res.format()


if __name__ == '__main__':
    requests = mp.Queue(cfg.MAX_QUEUE_SIZE)
    results = mp.Manager().dict()
    requests_lock = mp.Lock()
    results_lock = mp.Lock()

    for i in range(server_cfg.PROCESSES_COUNT):
        mp.Process(target=executor, args=(requests, results, requests_lock, results_lock)).start()

    app.run(host="10.0.0.5", port="8080")
