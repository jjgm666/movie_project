# coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.comfig["SQLALCHEMY_DATABASE_URI"] = "mysql://root;123456@127.0.0.1;8889/movie"
app.config["SQLAlCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)


# 会员的数据模型
class user(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)  # 手机号
    info = db.Column(db.Text)  # 个性简介
    face = db.Column(db.String(255), unique=True)  # 头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 注册时间
    uuid = db.Column(db.String(255), unique=True)  # 唯一标识符.
    userlogs = db.relationship('Userlog', backref='user')  # 外键关系关联


def __repr__(self):
    return "<user %r>" % self.name


# 会员登陆日志
class Userlog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属会员
    ip = db.Column(db.String(100))  # 最近登陆ip
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 最近登录时间

    def __repr__(self):
        return "<Userlog %r>" % self.id
