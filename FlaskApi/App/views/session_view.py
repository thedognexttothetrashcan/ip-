from flask import Blueprint, request, render_template, session, redirect, url_for

from App.models import Movie

blue = Blueprint("blue", __name__)


@blue.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form.get("username")

        session['username'] = username

        return redirect(url_for("blue.mine"))


@blue.route("/mine/")
def mine():
    if request.method == "GET":

        username = session.get("username")

        movies = Movie.query.all()

        return render_template("mine.html", username=username, movies=movies)


