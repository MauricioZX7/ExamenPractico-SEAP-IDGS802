from flask import Blueprint, render_template,redirect,url_for
from flask_security import login_required, current_user
from flask_security.decorators import roles_required, roles_accepted 
from flask import request
from . import db
from .models import Producto
#import forms
import base64

main = Blueprint("main",__name__)

@main.errorhandler(404)
def error_404(e):
    return render_template("404.html"),404

#Definimos la ruta para la página principal
@main.route("/")
def index():
    return render_template("index.html")

@main.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@main.route("/contacto")
def contacto():
    return render_template("contacto.html")

#Definimos la ruta para la página perfil de usuario
@main.route("/profile")
@login_required
#@roles_required
@roles_accepted("admin","user")
def profile():
    return render_template("profile.html", name=current_user.name)

@main.route("/productos")
@login_required
@roles_accepted("admin","user")
def getproductos():

    producto = Producto.query.all()

    return render_template("productos.html", productos=producto)


# Parte de administradores

@main.route("/agregarProducto")
@login_required
@roles_accepted("admin")
def agregar():
    file=""
    encoded_string = ""
    if request.method =="POST":
        file = request.form.get('imagen')
        if file:
            file_contents = file.read()
            encoded_string = base64.b64encode(file_contents).decode('utf-8')
            print(encoded_string)


        product =  Producto(nombreProducto=request.form.get("nombreProducto"),
                           categoria=request.form.get("categoria"),
                           descripcion=request.form.get("descripcion"),
                           unidadMedida=request.form.get("unidadMedida"),
                           marca=request.form.get("marca"),
                           precio=float(request.form.get("precio")),
                           imagen=encoded_string)
        db.session.add(product)
        db.session.commit()

        return redirect(url_for("profile.html"))
    return render_template("agregarProducto.html")
