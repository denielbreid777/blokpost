from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



class Post:
    def __init__(self, title, description):
        self.title = title
        self.description = description



posts_list = [
    Post("Bober", "Browse the libraries of Megascans and MetaHumans content in a quick and artist-friendly way through Bridge."),
    Post("Space X", "Fire up an all-new Bridge tab right inside of Unreal Engine 5 and drop optimized content directly into your project."),
    Post("NASA", "Seamlessly export to your favorite 3D application or game engine with one click. Save time and have fun creating."),
    Post("Blender", "Blender is the free and open source 3D creation suite."),
    Post("AI Future", "Artificial Intelligence is transforming the world. Here’s what’s coming."),
    Post("Python", "Python is a versatile and beginner-friendly programming language."),
    Post("Flask Magic", "Flask is a lightweight WSGI web application framework. It's easy to get started with!"),
]



@app.route("/")
def home():
    return render_template("index.html", posts=posts_list)



@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        if title and description:
            new_post = Post(title, description)
            posts_list.append(new_post)
            return redirect(url_for("home"))
    return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True)
