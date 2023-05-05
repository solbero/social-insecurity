"""Provides all routes for the Social Insecurity application.

This file contains the routes for the application. It is imported by the app package.
It also contains the SQL queries used for communicating with the database.
"""

import os
from datetime import datetime

from flask import flash, redirect, render_template, send_from_directory, url_for

from app import app, sqlite
from app.forms import CommentsForm, FriendsForm, IndexForm, PostForm, ProfileForm


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    """Provides the index page for the application.

    It reads the composite IndexForm and based on which form was submitted,
    it either logs the user in or registers a new user.

    If no form was submitted, it simply renders the index page.
    """
    form = IndexForm()

    if form.login.is_submitted() and form.login.submit.data:
        user = sqlite.query('SELECT * FROM Users WHERE username="{}";'.format(form.login.username.data), one=True)

        if user is None:
            flash("Sorry, this user does not exist!", category="warning")
        elif user["password"] == form.login.password.data:
            return redirect(url_for("stream", username=form.login.username.data))
        else:
            flash("Sorry, wrong password!", category="warning")

    elif form.register.is_submitted() and form.register.submit.data:
        sqlite.query(
            'INSERT INTO Users (username, first_name, last_name, password) VALUES("{}", "{}", "{}", "{}");'.format(
                form.register.username.data,
                form.register.first_name.data,
                form.register.last_name.data,
                form.register.password.data,
            )
        )
        flash("User successfully created!", category="success")
        return redirect(url_for("index"))

    return render_template("index.html.j2", title="Welcome", form=form)


@app.route("/stream/<string:username>", methods=["GET", "POST"])
def stream(username: str):
    """Provides the stream page for the application.

    If a form was submitted, it reads the form data and inserts a new post into the database.

    Otherwise, it reads the username from the URL and displays all posts from the user and their friends.
    """
    form = PostForm()
    user = sqlite.query('SELECT * FROM Users WHERE username="{}";'.format(username), one=True)

    if post_form.is_submitted():
        if post_form.image.data:
            path = os.path.join(app.instance_path, app.config["UPLOADS_FOLDER_PATH"], post_form.image.data.filename)
            post_form.image.data.save(path)

        sqlite.query(
            'INSERT INTO Posts (u_id, content, image, creation_time) VALUES({}, "{}", "{}", \'{}\');'.format(
                user["id"],
                form.content.data,
                form.image.data.filename,
                datetime.now(),
            )
        )
        return redirect(url_for("stream", username=username))

    posts = sqlite.query(
        "SELECT p.*, u.*, (SELECT COUNT(*) FROM Comments WHERE p_id=p.id) AS cc FROM Posts AS p JOIN Users AS u ON u.id=p.u_id WHERE p.u_id IN (SELECT u_id FROM Friends WHERE f_id={0}) OR p.u_id IN (SELECT f_id FROM Friends WHERE u_id={0}) OR p.u_id={0} ORDER BY p.creation_time DESC;".format(
            user["id"],
        )
    )
    return render_template("stream.html.j2", title="Stream", username=username, form=form, posts=posts)


@app.route("/comments/<string:username>/<int:p_id>", methods=["GET", "POST"])
def comments(username: str, p_id: str):
    """Provides the comments page for the application.

    If a form was submitted, it reads the form data and inserts a new comment into the database.

    Otherwise, it reads the username and post id from the URL and displays all comments for the post.
    """
    form = CommentsForm()

    if form.is_submitted():
        user = sqlite.query('SELECT * FROM Users WHERE username="{}";'.format(username), one=True)
        sqlite.query(
            "INSERT INTO Comments (p_id, u_id, comment, creation_time) VALUES({}, {}, \"{}\", '{}');".format(
                p_id,
                user["id"],
                form.comment.data,
                datetime.now(),
            )
        )

    post = sqlite.query("SELECT * FROM Posts WHERE id={};".format(p_id), one=True)
    all_comments = sqlite.query(
        "SELECT DISTINCT * FROM Comments AS c JOIN Users AS u ON c.u_id=u.id WHERE c.p_id={} ORDER BY c.creation_time DESC;".format(
            p_id,
        )
    )
    return render_template(
        "comments.html.j2", title="Comments", username=username, form=form, post=post, comments=all_comments
    )


@app.route("/friends/<string:username>", methods=["GET", "POST"])
def friends(username: str):
    """Provides the friends page for the application.

    If a form was submitted, it reads the form data and inserts a new friend into the database.

    Otherwise, it reads the username from the URL and displays all friends of the user.
    """
    form = FriendsForm()
    user = sqlite.query('SELECT * FROM Users WHERE username="{}";'.format(username), one=True)

    if form.is_submitted():
        friend = sqlite.query('SELECT * FROM Users WHERE username="{}";'.format(form.username.data), one=True)

        if friend is None:
            flash("User does not exist", category="warning")
        else:
            sqlite.query(
                "INSERT INTO Friends (u_id, f_id) VALUES({}, {});".format(
                    user["id"],
                    friend["id"],
                )
            )

    all_friends = sqlite.query(
        "SELECT * FROM Friends AS f JOIN Users as u ON f.f_id=u.id WHERE f.u_id={} AND f.f_id!={} ;".format(
            user["id"],
            user["id"],
        )
    )
    return render_template("friends.html.j2", title="Friends", username=username, friends=all_friends, form=form)


# see and edit detailed profile information of a user
@app.route("/profile/<string:username>", methods=["GET", "POST"])
def profile(username: str):
    """Provides the profile page for the application.

    If a form was submitted, it reads the form data and updates the user's profile in the database.

    Otherwise, it reads the username from the URL and displays the user's profile.
    """
    form = ProfileForm()

    if form.is_submitted():
        sqlite.query(
            'UPDATE Users SET education="{}", employment="{}", music="{}", movie="{}", nationality="{}", birthday=\'{}\' WHERE username="{}" ;'.format(
                form.education.data,
                form.employment.data,
                form.music.data,
                form.movie.data,
                form.nationality.data,
                form.birthday.data,
                username,
            )
        )
        return redirect(url_for("profile", username=username))

    user = sqlite.query(
        'SELECT * FROM Users WHERE username="{}";'.format(
            username,
        ),
        one=True,
    )
    return render_template("profile.html.j2", title="Profile", username=username, user=user, form=form)


@app.route("/uploads/<string:filename>")
def uploads(filename):
    """Provides an endpoint for serving uploaded files."""
    return send_from_directory(os.path.join(app.instance_path, app.config["UPLOADS_FOLDER_PATH"]), filename)
