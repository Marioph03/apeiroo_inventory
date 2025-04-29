from odoo import models, fields

class Category(models.Model):
# Nombre de la categoría
    name = fields.Char(
        string='Nombre',
        required=True,
    )