from base import db
from base.com.vo.uservo import userVo
from base.com.vo.postvo import postVo
from base.com.vo.comment import commentVo


class userDao:
    def get_name(self, data):
        name = userVo.query.filter_by(useremail=data).all()
        return name[0].username

    def login(self, data):
        email = userVo.query.filter_by(useremail=data.useremail).all()
        if len(email) != 0:
            password = userVo.query.filter_by(userpassword=data.userpassword).all()
            if len(password) != 0:
                ckhlist = userVo.query.filter_by(useremail=data.useremail, userpassword=data.userpassword).all()
                if len(ckhlist) != 0:
                    return "valid"
                else:
                    return "notvalid"
            else:
                return "password"
        else:
            return "email"

    def registeruser(self, userdata):
        db.session.add(userdata)
        db.session.commit()


class postDao:
    def getid(self, data):
        id = userVo.query.filter_by(useremail=data).all()
        return id[0].userid

    def updatepost(self, postdata):
        db.session.add(postdata)
        db.session.commit()

    def post(self):
        list = db.session.query(userVo, postVo).join(userVo, postVo.userid == userVo.userid).all()
        return list


class commentDao:
    def getid(self, data):
        id = userVo.query.filter_by(useremail=data).all()
        return id[0].userid

    def comment(self, comment):
        db.session.add(comment)
        db.session.commit()

    def comments(self, name):
        list = db.session.query(userVo, postVo, commentVo) \
            .join((userVo, commentVo.userid == userVo.userid)) \
            .join(postVo, commentVo.postid == postVo.postid) \
            .all()
        print(list)
        return list
