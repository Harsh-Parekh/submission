from base import db
from base.com.vo.uservo import userVo

class postVo(db.Model):
    __tablename__ = 'posttable'
    postid = db.Column('postid', db.Integer, primary_key=True, autoincrement=True)
    postitle = db.Column('postitle', db.String(100))
    postdescription = db.Column('postdescription', db.String(100))
    userid = db.Column('userid', db.Integer, db.ForeignKey(userVo.userid))

    def as_dict(self):
        return {
            'post_title': self.post_title,
            'postdescription': self.postdescription,
            'userid':self.userid
        }


db.create_all()
