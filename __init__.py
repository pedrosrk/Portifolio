from flask import Flask, render_template, redirect, url_for, request, flash
import nltk, os, cv2
import sqlite3 as sql
from apps import sentiment, detect

app = Flask(__name__)
app.secret_key='admin123'

## Home Page ##
@app.route("/")
def hello():
    return render_template('webPage/home.html')

@app.route("/skills")
def for_loop():
	list_of_courses = ['DevOps', 'Python', 'JavaScript', 'HTML', 'CSS', 'Jira', 'Git', 'GitHub', 'SQL', 'SCRUM']
	return render_template("webPage/skills.html", courses=list_of_courses)

@app.route("/jobs")
def features():
    return render_template('webPage/jobs.html')

@app.route("/blog")
def blog():
    con=sql.connect("dataBase/db_web.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from msgs")
    data=cur.fetchall()
    return render_template("blog/index_msg.html",datas=data)

@app.route("/add_msg",methods=['POST','GET'])
def add_msg():
    if request.method=='POST':
        uname=request.form['uname']
        contact=request.form['contact']
        con=sql.connect("dataBase/db_web.db")
        cur=con.cursor()
        cur.execute("insert into msgs(UNAME,CONTACT) values (?,?)",(uname,contact))
        con.commit()
        flash('msg Added','success')
        return redirect(url_for("blog"))
    return render_template("blog/add_msg.html")

@app.route("/edit_msg/<string:uid>",methods=['POST','GET'])
def edit_msg(uid):
    if request.method=='POST':
        uname=request.form['uname']
        contact=request.form['contact']
        con=sql.connect("dataBase/db_web.db")
        cur=con.cursor()
        print("hello")
        cur.execute("update msgs set UNAME=?,CONTACT=? where UID=?",(uname,contact,uid))
        con.commit()
        flash('msg Updated','success')
        return redirect(url_for("blog"))
    con=sql.connect("dataBase/db_web.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from msgs where UID=?",(uid,))
    data=cur.fetchone()
    return render_template("blog/edit_msg.html",datas=data)
    
@app.route("/delete_msg/<string:uid>",methods=['GET'])
def delete_msg(uid):
    con=sql.connect("dataBase/db_web.db")
    cur=con.cursor()
    cur.execute("delete from msgs where UID=?",(uid,))
    con.commit()
    flash('Msg Deleted','warning')
    return redirect(url_for("blog"))

@app.route("/contact")
def contact():
    return render_template('webPage/contact.html')

## Features ##
@app.route("/image")
def serve_image():
    message = "Image Route"
    return render_template('features/image.html', message=message)

@app.route("/audio")
def serve_audio():
    message = "Audio Route"
    return render_template('features/audio.html', message=message)

@app.route("/video")
def serve_video():
    message = "Video Route"
    return render_template('features/video.html', message=message)

@app.route("/sentiment", methods=['GET', 'POST'])
def work_sentiment():
    nltk.download('vader_lexicon')
    if request.method == 'GET':
        message = "Sentiment Analysis"
        obj1 = sentiment.Emotion()
        result = obj1.sentiment_scores_compound()
        return render_template('features/sentiment.html', message=message, result=result)
    else:
        message = "Sentiment Analysis"
        obj1 = sentiment.Emotion(request.form['message'])
        result = obj1.sentiment_scores_compound()
        return render_template('features/sentiment.html', message=message, result=result)

#detect object
@app.route("/detect", methods=['GET', 'POST'])
def detect_object():
    if request.method == 'POST':
        image_file = request.files['image']
        if image_file:
            current_dir =  os.path.dirname(os.path.realpath(__file__))
            image_path = os.path.join(current_dir, 'static', 'assets', image_file.filename)
            image_file.save(image_path)
            image = cv2.imread(image_path)
            _, extension = os.path.splitext(image_path)
            new_image_path = 'input' + extension
            cv2.imwrite(os.path.join(current_dir, 'static', 'assets', new_image_path), image)
            det = detect.ObjDetect(new_image_path)
            det.save_detect_picture()
            os.remove(image_path)
        return render_template('features/detectobj.html', image_url="static/assets/output.jpg")
    return render_template('features/detectobj.html', image_url="static/assets/agilim.PNG")

if __name__ == "__main__":
    app.run(debug=True)