from flask import Flask, jsonify, request
from model.twit import Twit


app = Flask(__name__)

twits = []


@app.route('/twit', methods=['POST'])
def create_twit():
    # Приходит запрос {'body': 'Hello World', 'author': '@aqaguy', 'id': 1}
    twit_json = request.get_json()
    twit = Twit(twit_json['body'], twit_json['author'], twit_json['id'])
    twits.append(twit)
    return jsonify({'status': 'success'})


@app.route('/twit', methods=['GET'])
def read_twits():
    serialised_twits = []
    for twit in twits:
        serialised_twits.append(twit.to_dict())
    return jsonify({"twits": serialised_twits})


@app.route('/twit/<int:twit_id>', methods=['GET'])
def read_the_twit(twit_id):
    for i in range(len(twits)):
        if twit_id == twits[i].id:
            return jsonify(twits[i].to_dict())


@app.route('/twit', methods=['PUT'])
def update_twit():
    twit_json = request.get_json()
    for i in range(len(twits)):
        if twit_json['id'] == twits[i].id:
            twits[i].body = twit_json['body']
            break
    return jsonify({'status': 'success'})


@app.route('/twit', methods=['DELETE'])
def delete_twit():
    twit_json = request.get_json()
    for i in range(len(twits)):
        if twit_json['id'] == twits[i].id:
            del twits[i]
            break
    return jsonify({'status': 'success'})


if __name__ == "__main__":
    app.run(debug=True)
