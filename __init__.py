from flask import Flask, render_template, redirect, url_for, request, flash
import sqlite3 as sql
from apps import sentiment as st

app = Flask(__name__)
app.secret_key='admin123'

## Home Page ##
@app.route("/")
def hello():
    return render_template('webPage/home.html')

@app.route("/skills")
def for_loop():
	list_of_courses = ['Python', 'JavaScript', 'HTML', 'CSS', 'Jira', 'SCRUM', 'Git', 'GitHub', 'SQL', 'Mentory']
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

@app.route("/sentiment")
def sentiment():
    message = "Sentiment Analysis"
    obj1 = st.sentiment()
    result = obj1.sentiment_scores_compound()
    return render_template('features/sentiment.html', message=message, result=result)

@app.route("/detect")
def detect():
    message = "Detect Object"
    return render_template('features/detectobj.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)