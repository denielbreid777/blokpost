from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)




class Posts():
    def __init__(self, title, description):
        self.title = title
        self.description = description


posts_list = [
    Posts("Bober", "Browse the libraries of Megascans and MetaHumans content in a quick and artist-friendly way through Bridge."),
    Posts("Space X", "Fire up an all-new Bridge tab right inside of Unreal Engine 5 and drop optimized content directly into your project."),
    Posts("Nasa", "Seamlessly export to your favorite 3D application or game engine with one click. Save time and have fun creating.")
]



app.route("/")
def home():

    render_template("index.html", posts=posts_list )


















if __name__ == "__main__":
    app.run(debug=True)