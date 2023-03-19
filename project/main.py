from flask import Blueprint, render_template
from flask_security import login_required, current_user
from flask_security.decorators import roles_required, roles_accepted 
from . import db

main = Blueprint("main",__name__)

#Definimos la ruta para la página principal
@main.route("/")
def index():
    return render_template("index.html")

#Definimos la ruta para la página perfil de usuario
@main.route("/profile")
@login_required
#@roles_required
@roles_accepted("admin","user")
def profile():
    return render_template("profile.html", name=current_user.name)

