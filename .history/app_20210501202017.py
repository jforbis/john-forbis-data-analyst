from flask import Flask, render_template, redirect, jsonify, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")
