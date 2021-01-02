from base import db


class userVo(db.Model):
    __tablename__ = 'usertable'
    userid = db.Column('userid', db.Integer, primary_key=True, autoincrement=True)
    username = db.Column('username', db.String(25))
    useremail = db.Column('useremail', db.String(25))
    userpassword = db.Column('userpassword', db.String(25))
    usergender = db.Column('usergender', db.String(25))
    profileimg = db.Column('profile', db.String(100))

    def as_dict(self):
        return {
            'username': self.username,
            'useremail': self.useremail,
            'userpassword': self.userpassword,
            'usergender': self.usergender
        }


db.create_all()
