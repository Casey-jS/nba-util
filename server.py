from flask import Flask, request, jsonify
import db_util as db_util
from flask_cors import CORS, cross_origin
import gamelogs

app = Flask(__name__)
cors = CORS(app, resources={r"/.*": {"origins": "http://localhost"}})

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_SUPPORTS_CREDENTIALS'] = True

stupid_cors = "Access-Control-Allow-Origin"

@app.route("/top10/<stat>/", methods=["GET"])

def top_players(stat):
    print(stat)
    if request.method == "GET":
        top_scorers = db_util.get_league_leaders(stat)
        response = jsonify(top_scorers)
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response


@app.route("/teams/", methods=["GET"])

def teams():
    if request.method == "GET":
        teams = db_util.get_teams()
        response = jsonify(teams)
        response.headers.add(stupid_cors, "*")
        return response

@app.route("/players/<playerID>/", methods=["GET"])

def get_player(playerID):
    if request.method == "GET":
        player_info = db_util.get_player_by_id(playerID)
        response = jsonify(player_info)
        response.headers.add(stupid_cors, "*")
        return response

@app.route("/teams/<teamID>/")

def get_roster(teamID):
    if request.method == "GET":
        roster = db_util.get_roster(teamID)
        response = jsonify(roster)
        response.headers.add(stupid_cors, "*")
        return response
@app.route("/validateuser/", methods=["POST", "GET", "OPTIONS"])
@cross_origin(origins='*')

def validate_user():
    if request.method == "POST":
        data = request.json
        userName = data["username"]
        password = data["password"]
        print("Got username " + userName + " and password " + password)
        valid: bool = db_util.user_exists(userName) and db_util.validate_user(userName, password)
        print("User is valid: ", valid)
        dict_to_send = {"is_valid" : valid}
        json_to_send = jsonify(dict_to_send)
        return json_to_send

@app.route("/last5/<playerID>/", methods=["GET"])

def last_5_games(playerID):
    if request.method == "GET":
        last5_list = gamelogs.get_game_logs(playerID)
        response = jsonify(last5_list)
        return response


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    header['Access-Control-Allow-Methods'] = 'OPTIONS, HEAD, GET, POST, DELETE, PUT'
    return response



    





    
    



        

