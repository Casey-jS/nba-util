from flask import Flask, request, jsonify
import db_util as db_util

app = Flask(__name__)

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

""" @app.route("/players/<id:int>/")

def player(id):
    if request.method == "GET":
        player = db_util.get_player(id)
        response = jsonify(player)
        response.headers.add(stupid_cors, "*") """


        

