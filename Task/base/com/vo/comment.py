from base import db
from base.com.vo.uservo import userVo
from base.com.vo.postvo import postVo


class commentVo(db.Model):
    __tablename__ = 'comments'
    commentid = db.Column('qnaid', db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column('comment', db.String(100))
    userid = db.Column('userid', db.Integer, db.ForeignKey(userVo.userid))
    postid = db.Column('postid', db.Integer, db.ForeignKey(postVo.postid))

    def as_dict(self):
        return {
            'comment': self.comment,
            'userid': self.userid
        }


db.create_all()
