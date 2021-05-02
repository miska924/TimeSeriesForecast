from pprint import pprint
from flask import request, Flask

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    pprint(dict(request.form))
    return "OK"
