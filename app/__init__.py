# coding:utf-8
from flask import Flask

app = Flask(__name__)  #实例化flask
app.debug = True   #  开启调试模式

from app.home import home as home_blueprint      #  从app导入home对象
from app.admin import admin as admin_blueprint   #  从app导入admin对象

app.register_blueprint(home_blueprint)        #注册home蓝图
app.register_blueprint(admin_blueprint, url_prefix="/admin")    #注册admin蓝图
