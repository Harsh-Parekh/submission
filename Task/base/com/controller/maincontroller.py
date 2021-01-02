from base import app, render_template, redirect, url_for, request, session, flash
from base.com.dao.operationDao import userDao, postDao, commentDao
from base.com.vo.uservo import userVo
from base.com.vo.postvo import postVo
from base.com.vo.comment import commentVo
import os


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/logout')
def logout():
    session['logged_in'] = 'logout'
    session.pop('user')
    return redirect(url_for('index'))


@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/render')
def home():
    if session['logged_in'] == "logged":
        return render_template('home.html')
    else:
        return redirect(url_for('index'))


@app.route('/comment/<int:id>')
def comment(id):
    return render_template('comment.html', id=id)


@app.route('/register')
def register():
    return render_template('registration.html')


@app.route('/register_user', methods=["POST"])
def register_user():
    obj_dao = userDao()
    obj_vo = userVo()
    obj_vo.username = request.form.get('username')
    obj_vo.useremail = request.form.get('useremail')
    obj_vo.userpassword = request.form.get('userpassword')
    obj_vo.usergender = request.form.get('usergender')
    file = request.files['file']
    filename = file.filename
    obj_vo.profileimg = filename
    file.save(os.path.join(r"/home/spy/work/Tasksubmission/Task/img", filename))
    obj_dao.registeruser(obj_vo)
    flash('You have successfully registered')
    return redirect(url_for('index'))


@app.route('/login', methods=["POST"])
def Login():
    obj_dao = userDao()
    obj_vo = userVo()
    obj_vo.useremail = request.form.get('email')
    obj_vo.userpassword = request.form.get('password')
    result = obj_dao.login(obj_vo)
    if result == "valid":
        session['logged_in'] = "logged"
        session['user'] = request.form.get('email')
        return redirect(url_for('home'))
    elif result == "notvalid":
        data = "Invalid Username and password...!"
        flash(data)
        return redirect(url_for('index'))
    elif result == "password":
        data = "Invalid password...!"
        flash(data)
        return redirect(url_for('index'))

    elif result == "email":
        data = "Invalid email...!"
        flash(data)
        return redirect(url_for('index'))


@app.route('/updatepost', methods=["POST"])
def updatepost():
    if session['logged_in'] == "logged":
        obj_vo = postVo()
        obj_dao = postDao()
        obj_vo.postitle = request.form.get('postitle')
        obj_vo.postdescription = request.form.get('postdescription')
        user = session['user']
        id = obj_dao.getid(user)
        obj_vo.userid = id
        obj_dao.updatepost(obj_vo)
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))


@app.route('/seepost')
def seepost():
    obj_dao = postDao()
    result = obj_dao.post()
    return render_template('postdata.html', post=result)


@app.route('/addcomment', methods=["POST"])
def addcomment():
    if session['logged_in'] == "logged":
        postid = request.form.get('id')
        obj_vo = commentVo()
        obj_dao = commentDao()
        obj_vo.comment = request.form.get('comment')
        user = session['user']
        id = obj_dao.getid(user)
        obj_vo.userid = id
        obj_vo.postid = postid
        obj_dao.comment(obj_vo)
        return redirect(url_for('seepost'))
    else:
        return redirect(url_for('home'))


@app.route('/viewcomment')
def viewcomment():
    if session['logged_in'] == "logged":
        obj_dao = commentDao()
        result = obj_dao.comments()
        return render_template('reviews.html', comment=result)
    else:
        return redirect(url_for('home'))
 
