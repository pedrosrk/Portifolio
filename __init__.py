from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('webPage/home.html')

@app.route("/skills")
def for_loop():
	list_of_courses = ['Python', 'JavaScript', 'HTML', 'CSS', 'Jira', 'SCRUM', 'Git', 'GitHub', 'SQL']
	return render_template("webPage/skills.html", courses=list_of_courses)

@app.route("/jobs")
def features():
    return render_template('webPage/jobs.html')

@app.route("/contact")
def contact():
    return render_template('webPage/contact.html')

@app.route("/video")
def serve_video():
    message = "Video Route"
    return render_template('webPage/video.html', message=message)
  
@app.route("/audio")
def serve_audio():
    message = "Audio Route"
    return render_template('webPage/audio.html', message=message)
  
@app.route("/image")
def serve_image():
    message = "Image Route"
    return render_template('webPage/image.html', message=message)

if __name__ == "__main__":
	app.run(debug=True)