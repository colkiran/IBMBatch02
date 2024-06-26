
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
        return {player:players[player]}

api.add_resource(Players, "/getplayer/<string:player>")

if __name__ == '__main__':
    app.run(debug=True)








