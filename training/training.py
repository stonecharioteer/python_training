# -*- coding: utf-8 -*-
from flask import (Flask, render_template, 
    redirect, url_for, request, session, 
    abort, flash, jsonify)

app = Flask(__name__)

@app.route("/")
def serve_index():
    """Serves the index page."""
    return render_template("home.html")

@app.route("/home")
def serve_home():
    """Serves the home page."""
    return render_template("home.html")


