from pprint import pprint
from flask import request, Flask

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():

    return "OK"


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
    app.run(host="10.0.0.5", port="8080")
