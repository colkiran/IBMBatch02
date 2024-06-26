import json

from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

players = {
    'sachin' :{'name' :'Sacin Tendulkar', 'runs': 34850, 'matches':850, 'wickets': 350},
    'ponting':{'name': 'Ricky Ponting', 'runs':26580, 'wickets': 150},
    'lara': {'name': 'Brain Lara', 'runs': 23400, 'wickets': 120}
}

class Players(Resource):

    def get(self, player):
        return {player: players[player]}

    def put(self, player):
        players[player]['team'] = request.form['team']
        return {'result':players[player]}

    def patch(self, player):
        data1 = request.json
        data = json.loads(data1)
        players[player][list(data.keys())[0]] = data[list(data.keys())[0]]
        return players[player]

    def post(self, player):
        data1 = request.json
        data = json.loads(data1)
        print(data)
        players[player] = data
        return players

    def delete(self, player):
        if player in players:
            del players[player]

            return {'result': players}
        else:
            return {'KeyError': "Invalid key, Please enter a valid key....."}

api.add_resource(Players, "/getplayer/<string:player>")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)








