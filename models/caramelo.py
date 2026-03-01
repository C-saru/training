from odoo import models,fields

class caramelazaa(models.Model):
    __name= "caramelos_zaza" 
    __description="ogabooogaaaa"

    name = fields.Char(string = "caramelo de 1 bolivar",required = True )
    descripcion = fields.Char(string = 'caramelo baratongo')
    disponible = fields.boolean(string = 'disponible',default = True)
    cantidad = fields.float(string= 'cantidad de caramelos',default = 1.0)