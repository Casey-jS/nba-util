from flask import Flask, request, jsonify
import db_util as db_util
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/.*": {"origins": "http://localhost"}})

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_SUPPORTS_CREDENTIALS'] = True

stupid_cors = "Access-Control-Allow-Origin"

global_user = ""

@app.route("/getuser/")

def get_user():
    if request.method== "GET":
        response = jsonify({"user" : global_user})
        response.headers.add(stupid_cors, "*")
        return response

@app.route("/top4/<stat>/")
def top4_players(stat):
    if request.method == "GET":
        top4 = db_util.get_top4_stat(stat)
        print("Got request for top4 stats")
        response = jsonify(top4)
        response.headers.add(stupid_cors, "*")
        return response

# returns the top 30 players for a given stat
@app.route("/top10/<stat>/", methods=["GET"])
def top_players(stat):
    print(stat)
    if request.method == "GET":
        top_scorers = db_util.get_league_leaders(stat)
        response = jsonify(top_scorers)
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

# returns all of the teams' stats
@app.route("/teams/", methods=["GET"])
def teams():
    if request.method == "GET":
        teams = db_util.get_teams()
        response = jsonify(teams)
        response.headers.add(stupid_cors, "*")
        return response

# returns common team info (name, wins, losses)
@app.route("/teaminfo/<teamID>/")
def team_info(teamID):
    if request.method == "GET":
        info = db_util.get_team_info(teamID)
        response = jsonify(info)
        response.headers.add(stupid_cors, "*")
        return response

# returns a player given their id
@app.route("/players/<playerID>/", methods=["GET"])
def get_player(playerID):
    if request.method == "GET":
        player_info = db_util.get_player_by_id(playerID)
        response = jsonify(player_info)
        response.headers.add(stupid_cors, "*")
        return response

# returns a teams' roster
@app.route("/teams/<teamID>/")
def get_roster(teamID):
    if request.method == "GET":
        roster = db_util.get_roster(teamID)
        response = jsonify(roster)
        response.headers.add(stupid_cors, "*")
        return response

# returns true if a user is valid
@app.route("/validateuser/", methods=["POST", "GET", "OPTIONS"])
@cross_origin(origins='*')
def validate_user():
    global global_user
    if request.method == "POST":
        data = request.json
        userName = data["username"]
        password = data["password"]
        print("Got username " + userName + " and password " + password)
        valid: bool = db_util.user_exists(userName) and db_util.validate_user(userName, password)

        if valid:
             global_user = userName
             dict_to_send = {"is_valid" : valid, "user" : userName}
        else:
            dict_to_send = {"is_valid" : valid, "user" : ""}
        json_to_send = jsonify(dict_to_send)
        return json_to_send

# adds a new favorite player to the db
@app.route("/newfavplayer/", methods=["POST", "GET"])
def add_new_fav_player():
    if request.method == 'POST':
        data = request.json
        user = data['userName']
        playerID = data['player']
        db_util.new_fav_player(user, playerID)
        return jsonify({"success" : True})

# returns all favorite players for a user
@app.route("/favplayers/<userName>/", methods=["GET"])
def fav_players(userName):
    if request.method == "GET":
        players_list = db_util.get_fav_players(userName)
        if players_list == None:
            response = jsonify({"found": False})
            response.headers.add(stupid_cors, "*")
            return response
        # if there is a valid list of players
        response = jsonify(players_list)
        response.headers.add(stupid_cors, "*")
        return response
        

""" # returns the last 5 game logs for a player
@app.route("/last5/<playerID>/", methods=["GET"])
def last_5_games(playerID):
    if request.method == "GET":
        last5_list = gamelogs.get_last5(playerID)
        response = jsonify(last5_list)
        return response """

# adds a user to the db
@app.route("/signup/", methods=["POST", "GET"])
def new_account():
    if request.method == "POST":
        data = request.json
        username = data['userName']
        password = data['password']
        db_util.new_user(username, password)

@app.route("/signout/")
def sign_out():
    global global_user
    global_user = ""
    response = jsonify({"signout" : True})
    response.headers.add(stupid_cors, "*")
    return response

@app.route("/teamlogs/<teamID>/", methods=["GET"])

def get_teamlogs(teamID):
    if request.method == "GET":
        last5_list = db_util.get_team_log(teamID)
        response = jsonify(last5_list)
        response.headers.add(stupid_cors, "*")
        return response

@app.route("/standings/<conf>/", methods=["GET"])
def get_west_standings(conf):
    conference = ""
    if conf == '0':
        conference = 'West'
    else:
        conference = 'East'

    print("Getting stats for " + conference + " teams")
    standings = db_util.get_standings(conference)
    response = jsonify(standings)
    response.headers.add(stupid_cors, "*")
    return response

@app.route("/isfavorited/", methods=["GET", "POST"])

def is_favorited():
    if request.method == "POST":
        data = request.json
        user = data['userName']
        playerID = data['playerID']
        exists = db_util.is_favorited(user, playerID)
        return jsonify({"is_favorited", exists})


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    header['Access-Control-Allow-Methods'] = 'OPTIONS, HEAD, GET, POST, DELETE, PUT'
    return response






    





    
    



        

