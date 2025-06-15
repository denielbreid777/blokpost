from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)




class Post:
    def __init__(self, title, description, author, comment=[]):
        self.title = title
        self.description = description
        self.author = author
        self.likes = 0
        self.comment = comment

posts_list = [
    Post("Bober", "Browse the libraries of Megascans and MetaHumans content in a quick and artist-friendly way through Bridge.", "", []),
    Post("Space X", "Fire up an all-new Bridge tab right inside of Unreal Engine 5 and drop optimized content directly into your project.", "", []),
    Post("NASA", "Seamlessly export to your favorite 3D application or game engine with one click. Save time and have fun creating.", "", []),
    Post("Blender", "Blender is the free and open source 3D creation suite.", "", []),
    Post("AI Future", "Artificial Intelligence is transforming the world. Here’s what’s coming.", "", []),
    Post("Python", "Python is a versatile and beginner-friendly programming language.", "", []),
    Post("Flask Magic", "Flask is a lightweight WSGI web application framework. It's easy to get started with!", "", []),
]



@app.route("/")
def home():
    msg = request.args.get("msg")

    return render_template("index.html", posts=posts_list, msg=msg, user=request.cookies.get("user_name", None))





@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        author = request.form.get("author")
        if title and description and author:
            new_post = Post(title, description, author)
            posts_list.append(new_post)
            return redirect(url_for("home"))
    return render_template("create.html")



@app.route("/like", methods=["POST"])
def like():
    like = int(request.form.get("like"))
    post_name = request.form.get("name")

    for post in posts_list:
        if post.title == post_name:
            if post.likes != 1:
                post.likes += like
    return redirect(url_for("home"))



@app.route("/auth")
def auth():
    user_name = request.args.get("name")
    user_pass = request.args.get("password")
    user_status = request.args.get("user_status", None)

    if user_status == "active":
        return render_template("acount.html", name=request.cookies.get("user_name"), password=request.cookies.get("password"))


    if user_name and user_pass:
        if user_name == request.cookies.get("user_name") and user_pass == request.cookies.get("password"):
            return render_template("acount.html", name=request.cookies.get("user_name"), password=request.cookies.get("password"))
        else:
            return redirect(url_for("reg", msg="This user is not exist. You need to register!"))
        
    return render_template("auth.html")




@app.route("/reg", methods=["GET","POST"])
def reg():
    msg = request.args.get("msg", None)

    if request.method == "GET":
        return render_template("reg.html", msg=msg)


    new_user_name = request.form.get("name")
    new_user_pass = request.form.get("password")

    saved_user_name = request.cookies.get("user_name")
    saved_user_password = request.cookies.get("password")

    if new_user_name and new_user_pass:
            if new_user_name == saved_user_name and new_user_pass == saved_user_password:
                return render_template("reg.html", msg="You're already registered. Try to login!")
            
            else:
                response = make_response(redirect(url_for("home", msg="You are sucsessfully registered")))
                response.set_cookie("user_name", new_user_name)
                response.set_cookie("password", new_user_pass)
                return response


                
@app.route("/comment")
def comment():
    title = request.args.get("title")
    comment = request.args.get("comment")

    for post in posts_list:
        if post.title == title:
            post.comment.append(comment)
    return redirect(url_for("home"))



@app.route("/out")
def out():
    response = make_response(redirect(url_for("home")))
    response.delete_cookie("user_name")
    response.delete_cookie("password")
    return response

    







if __name__ == "__main__":
    app.run(debug=True)



