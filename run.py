from flask import Flask, request, json
from app import app
from app import config

if __name__ == '__main__':
    app.run(debug=config['DEBUG'])
