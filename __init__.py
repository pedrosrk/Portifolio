from flask import Flask, render_template, redirect, url_for, request, flash
import sqlite3 as sql

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

@app.route("/index")
def index():
    con=sql.connect("dataBase/db_web.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from users")
    data=cur.fetchall()
    return render_template("user/index_user.html",datas=data)

@app.route("/add_user",methods=['POST','GET'])
def add_user():
    if request.method=='POST':
        uname=request.form['uname']
        contact=request.form['contact']
        con=sql.connect("dataBase/db_web.db")
        cur=con.cursor()
        cur.execute("insert into users(UNAME,CONTACT) values (?,?)",(uname,contact))
        con.commit()
        flash('User Added','success')
        return redirect(url_for("index"))
    return render_template("user/add_user.html")

@app.route("/edit_user/<string:uid>",methods=['POST','GET'])
def edit_user(uid):
    if request.method=='POST':
        uname=request.form['uname']
        contact=request.form['contact']
        con=sql.connect("dataBase/db_web.db")
        cur=con.cursor()
        print("hello")
        cur.execute("update users set UNAME=?,CONTACT=? where UID=?",(uname,contact,uid))
        con.commit()
        flash('User Updated','success')
        return redirect(url_for("index"))
    con=sql.connect("dataBase/db_web.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from users where UID=?",(uid,))
    data=cur.fetchone()
    return render_template("user/edit_user.html",datas=data)
    
@app.route("/delete_user/<string:uid>",methods=['GET'])
def delete_user(uid):
    con=sql.connect("dataBase/db_web.db")
    cur=con.cursor()
    cur.execute("delete from users where UID=?",(uid,))
    con.commit()
    flash('User Deleted','warning')
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.secret_key='admin123'
    app.run(debug=True)