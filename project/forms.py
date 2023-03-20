from wtforms import Form
from wtforms import StringField, IntegerField, FloatField
from wtforms import validators
from wtforms import FileField, TextAreaField



class Producto(Form):
    id=IntegerField("Id")
    nombre_producto = StringField("Producto")
    categoria = StringField("Categoría")
    descripcion = TextAreaField("Descripción")
    unidad_medida = StringField("Unidad de medida")
    marca = StringField("Marca")
    precio = FloatField("Precio")
    imagen = FileField("Imagen")




