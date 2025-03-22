from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blogs = response.json()
    return render_template("index.html", blogs=blogs)


def find_blog(blog_id):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blogs = response.json()
    for blog in blogs:
        if int(blog['id']) == int(blog_id):
            post = Post(blog_id=blog['id'],
                        title=blog['title'],
                        subtitle=blog['subtitle'],
                        body=blog['body'])
            return post


@app.route('/post/<blog_id>')
def show_post(blog_id):
    post = find_blog(blog_id=blog_id)
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
