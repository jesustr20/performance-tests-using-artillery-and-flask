from flask import Flask, jsonify, request
from dotenv import load_dotenv
from pathlib import Path
import flask

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)


@app.route('/api/v1/post', methods=['POST'])
def post_id():
  id = request.json['id']
  print(id)
  return flask.jsonify({'response':{'id': id}})


@app.route('/api/v1/get', methods=['GET'])
def get_id():
  id = request.args.get('id')
  return jsonify({'response':{'id': id}})



if __name__ == '__main__':
  app.run()