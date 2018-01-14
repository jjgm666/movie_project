# incoding:utf-8
from . import admin


@admin.route("/")
def index():
    return "<h1 style='color:blue'>This is Admin!</h1>"
