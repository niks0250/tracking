from flask import Flask, jsonify,request

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'medha aggarwal'

    return app
