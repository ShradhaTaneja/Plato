from flask import Flask, request, json

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test():
    return 'This is a test!'


if __name__ == '__main__':
    app.run(debug=True)

