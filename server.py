from flask import Flask, request, jsonify
import db_util as db_util


app = Flask(__name__)

@app.route("/top10/<stat>/", methods=["GET"])

def top_10_ppg(stat):
    print(stat)
    if request.method == "GET":
        top_scorers = db_util.get_league_leaders(stat)
        response = jsonify(top_scorers)
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response


        

