from flask import request, Flask, render_template, redirect
from date_base import Db
from flask.helpers import flash, url_for


# База данных
def date_base():
    db = Db()
    return db.db()

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret key"

@app.route("/",  methods=["GET", "POST"])
def main():
    return render_template("index.html")

# Создание поста 
@app.route('/create/', methods=["GET", "POST"]) # Разрешение на запрос
def create_post():
    if request.method.upper() != "POST":
        return render_template("create.html")
    title = request.form.get("title")
    content = request.form.get("content")

    if (
        title is None
        or content is None
        or title.strip() == ""
        or content.strip() == ""
    ):
        # flashes a message to tell the user to fill all the fields
        flash("Please fill all the fields")
        return render_template("create.html")
    Db().create_post(title, content)
    return redirect(url_for("display_posts"))

# Показывает все посты
@app.route("/posts/",  methods=["GET", "POST"])
def display_posts():
    posts = Db().display_posts()
    return render_template("posts.html", posts=posts)

# Показывает один определённый пост
@app.route("/posts/<int:post_id>")
def display_post(post_id):
    post = Db().display_post(post_id)
    return render_template("post.html", post=post, post_id=post_id)

# Удаляет пост
@app.route("/posts/<int:post_id>/delete")
def delete_post(post_id):
    Db().delete_post(post_id)
    return redirect(url_for("display_posts"))

# Редактирование пост
@app.route("/posts/<int:post_id>/edit", methods=["POST", "GET"])
def edit_post(post_id):
    post = Db().display_post(post_id)

    if request.method.upper() == "POST":
        title = request.form.get("title")
        content = request.form.get("content")

        if (
            title is None
            or content is None
            or title.strip() == ""
            or content.strip() == ""
        ):
            flash("Please fill all the fields")
            return render_template("edit.html", post=post)
        Db().edit_post(title, content, post_id)
        return redirect(url_for("display_posts"))
    return render_template("edit.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
