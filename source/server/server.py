import multiprocessing as mp
import uuid

from pprint import pprint
from flask import request, Flask

from source import config as cfg
from source.back.back import predictor

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    uid = str(uuid.uuid4())
    requests.put({
        'data': dict(request.form),
        'id': uid
    })

    return {
        "success": True,
        "id": uid
    }


@app.route('/test', methods=['POST'])
def test():
    return "OK"


@app.route('/get', methods=['GET'])
def get():
    if 'id' not in request.args:
        return {
            'status': cfg.Status.fail
        }

    if request.args['id'] in predictions:
        try:
            return {
                'data': predictions[request.args['id']]['data'],
                'status': cfg.Status.ready,
            }
        except:
            # TODO: rewrite it for correction
            return {
                "status": cfg.Status.wait
            }
    else:
        # TODO: it can be timeouted
        return {
            "status": cfg.Status.wait
        }


if __name__ == '__main__':
    requests = mp.Queue(cfg.MAX_QUEUE_SIZE)
    predictions = mp.Manager().dict()
    mp.Process(target=predictor, args=(requests, predictions)).start()

    app.run(host="10.0.0.5", port="8080")
