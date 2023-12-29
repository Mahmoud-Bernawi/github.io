from flask import Flask, render_template
import requests

app = Flask(__name__)


# main home page
@app.route('/')
def home():
    url = "https://api.npoint.io/9419b235bcc5a1fc52ae"
    data = requests.get(url)
    results = data.json()
    return render_template("index.html", file=results)


# about page
@app.route("/about")
def about():
    return render_template("about.html")


# contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:num>")
def post(num):
    url = "https://api.npoint.io/9419b235bcc5a1fc52ae"
    data = requests.get(url)
    results = data.json()

    # Find the specific blog post based on the provided num
    selected_blog = None
    for blog in results:
        if blog["id"] == num:
            selected_blog = blog
            break

    return render_template("post.html", blog=selected_blog)


if __name__ == "__main__":
    app.run(debug=True)
