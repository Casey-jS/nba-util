from flask import Flask, render_template, request
import db_util


app = Flask(__name__)

@app.route("/")

def top_10_ppg(methods=["POST", "GET"]):
    if request.method == "GET":
        top_scorers = db_util.get_league_leaders("ppg")
        js = db_util.get_data_json(top_scorers)
        return js
        

