from flask import Blueprint, render_template,redirect,url_for
from flask_security import login_required, current_user
from flask_security.decorators import roles_required, roles_accepted 
from flask import request
from . import db
from .models import Producto, User
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

@main.route("/agregarProducto", methods=["GET","POST"])
@login_required
@roles_accepted("admin")
def agregar():
    if request.method =="POST":
        img = request.files['imagen']
        img_str = base64.b64encode(img.read())
        img_b64 = img_str.decode("utf-8")
        print(img_str)
        print(img_b64)
        


        product =  Producto(nombreProducto=request.form.get("nombreProducto"),
                           categoria=request.form.get("categoria"),
                           descripcion=request.form.get("descripcion"),
                           unidadMedida=request.form.get("unidadMedida"),
                           marca=request.form.get("marca"),
                           precio=float(request.form.get("precio")),
                           imagen=img_b64)
        
        db.session.add(product)
        db.session.commit()
    
    producto = Producto.query.all()

    return render_template("agregarProducto.html", productos=producto)


@main.route("/modificarProducto", methods=["GET","POST"])
@login_required
def modificarPr():

    if request.method=="GET":
        id=request.args.get("id")
        producto=db.session.query(Producto).filter(Producto.id==id).first()

        idp = id
        nombrep = producto.nombreProducto
        cat =producto.categoria
        despc = producto.descripcion
        unit = producto.unidadMedida
        marca =producto.marca
        precio = producto.precio
        imagen = producto.imagen
        
    if request.method=="POST":

        img = request.files['imagen']
        img_str = base64.b64encode(img.read())
        img_b64 = img_str.decode("utf-8")
        
        id=request.form.get("id")
        
        product=db.session.query(Producto).filter(Producto.id==id).first()

        product.nombreProducto = request.form.get("nombreProducto")
        product.categoria = request.form.get("categoria")
        product.descripcion = request.form.get("descripcion")
        product.unidadMedida = request.form.get("unidadMedida")
        product.marca = request.form.get("marca")
        product.precio = float(request.form.get("precio"))
        product.imagen = img_b64

        db.session.add(product)
        db.session.commit()

        return redirect(url_for("main.agregar"))

    return render_template("modificarProducto.html", idp=idp, nombrep=nombrep,cat=cat, despc=despc, unit=unit, marca=marca, precio=precio, imagen=imagen)

@main.route("/eliminarProducto", methods=["GET","POST"])
@login_required
def eliminarPr():

    if request.method=="GET":
        id=request.args.get("id")
        producto=db.session.query(Producto).filter(Producto.id==id).first()

        idp = id
        nombrep = producto.nombreProducto
        cat =producto.categoria
        despc = producto.descripcion
        unit = producto.unidadMedida
        marca =producto.marca
        precio = producto.precio
        imagen = producto.imagen
        
    if request.method=="POST":
        
        id=request.form.get("id")
        
        product=db.session.query(Producto).filter(Producto.id==id).first()

        product.nombreProducto = request.form.get("nombreProducto")
        product.categoria = request.form.get("categoria")
        product.descripcion = request.form.get("descripcion")
        product.unidadMedida = request.form.get("unidadMedida")
        product.marca = request.form.get("marca")
        product.precio = float(request.form.get("precio"))
        product.imagen = "img_b64"

        db.session.delete(product)
        db.session.commit()

        return redirect(url_for("main.agregar"))

    return render_template("eliminarProducto.html", idp=idp, nombrep=nombrep,cat=cat, despc=despc, unit=unit, marca=marca, precio=precio, imagen=imagen)

