from flask import Flask, Response, request
from flask.ext.mako import render_template
from flask.ext.login import login_required
from app import application


@application.route("/")
def index():
	return render_template("index.html")
