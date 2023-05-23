from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('variable_example.html')

@app.route("/default")
def default():
	return render_template("layout.html")

@app.route("/var")
def var():
	user = "Geeksforgeeks"
	return render_template("variable_example.html", name=user)

@app.route("/ifelse")
def ifelse():
	user = "Pedrim"
	return render_template("if_example.html", name=user)

@app.route("/for_loop")
def for_loop():
	list_of_courses = ['Java', 'Python', 'C++', 'MATLAB']
	return render_template("for_example.html", courses=list_of_courses)

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