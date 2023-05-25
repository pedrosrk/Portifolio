from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/skills")
def for_loop():
	list_of_courses = ['Python', 'JavaScript', 'HTML', 'CSS', 'Jira', 'SCRUM', 'Git', 'GitHub', 'SQL']
	return render_template("for_example.html", courses=list_of_courses)

@app.route("/jobs")
def features():
    return render_template('jobs.html')

@app.route("/ifelse")
def ifelse():
	user = "Pedrim" # Variable example
	return render_template("if_example.html", name=user)

@app.route("/choice/<pick>")
def choice(pick):
	if pick == 'variable':
		return redirect(url_for('var'))
	if pick == 'if':
		return redirect(url_for('ifelse'))
	if pick == 'for':
		return redirect(url_for('for_loop'))
	
@app.route("/video")
def serve_video():
    message = "Video Route"
    return render_template('video.html', message=message)
  
@app.route("/audio")
def serve_audio():
    message = "Audio Route"
    return render_template('audio.html', message=message)
  
@app.route("/image")
def serve_image():
    message = "Image Route"
    return render_template('image.html', message=message)

if __name__ == "__main__":
	app.run(debug=True)