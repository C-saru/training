from odoo import models,fields

class caramelazaa(models.Model):
    _name= "caramelos.zaza" 
    _description="ogabooogaaaa"

    name = fields.Char(string = "caramelo de 1 bolivar",required = True )
    descripcion = fields.Char(string = 'caramelo baratongo')
    disponible = fields.Boolean(string = 'disponible',default = True)
    cantidad = fields.Float(string= 'cantidad de caramelos',default = 1.0)
    precio = fields.Float(string = 'precio',default = 1.0)  