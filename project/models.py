#Importamos el objeto de la base de datos __init__.py
from . import db
from flask_sqlalchemy import SQLAlchemy
#Importamos la clase UserMixin de  flask_login
from flask_security import UserMixin, RoleMixin

users_roles = db.Table("user_roles",
    db.Column("userId", db.Integer, db.ForeignKey("user.id")),
    db.Column("roleId", db.Integer, db.ForeignKey("role.id")))

class User(UserMixin, db.Model):
    """User account model."""

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean)
    confirmed_at = db.Column(db.DateTime)
    roles = db.relationship("Role",
        secondary=users_roles,
        backref=db.backref("users", lazy="dynamic"))
    
class Role(RoleMixin, db.Model):
    """Role model"""

    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description=db.Column(db.String(255))

class Producto(db.Model):
    __tablename__= "producto"
    id = db.Column(db.Integer, primary_key=True)
    nombreProducto = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(255))
    unidadMedida = db.Column(db.String(50))
    marca = db.Column(db.String(50))
    precio = db.Column(db.Float)
    imagen = db.Column(db.LargeBinary(length=20971520))





















#class User(UserMixin, db.Model):
"""User account model."""
     
