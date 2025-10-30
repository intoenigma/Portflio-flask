from flask import Flask, redirect, render_template

web = Flask(__name__)

@web.route("/")
def index():
    return redirect ("/home")

@web.route("/home")
def home():
    title = "Into Enigma"
    content_heading = "Welcome To the Webpage Where Things You Can't UNSEEN!"
    content_paragraph = "Behind intoenigma lies curiosity — the drive to uncover patterns, emotions, and meaning through creation. This portfolio is not just a display of work, but a glimpse into how I see and shape the unseen."
    return render_template("/home.html",title = title , content_heading = content_heading, content_paragraph = content_paragraph)

@web.route("/projects")
def projects():
    projects = [
        {
            "title": "IntoEnigma Website",
            "description": "A sleek, modern personal site built with Flask, HTML, and pure CSS — featuring custom gradients and animations.",
            "image_url": "https://i.ibb.co/XrHDM0W4/project-preview.png",
            "demo_url": "https://your-live-demo-link.com",
            "github_url": "https://github.com/yourusername/intoenigma",
        }
    ]
    return render_template("projects.html", projects=projects)



@web.route("/contacts")
def contact():
    return render_template ("/contact.html")



if __name__ == "__main__":
    web.run( debug = True)