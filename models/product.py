from odoo import models, fields


class Product(models.Model):
   # name: nombre del producto
    name = fields.Char(
        string='Nombre',
        required=True,
    )
    # entry_date: fecha de entrada
    entry_date = fields.Date(
        string='Fecha de Entrada',
        required=True,
    )
    # exit_date: fecha de salida (puede quedar vacía si aún no se ha salido)
    exit_date = fields.Date(
        string='Fecha de Salida',
    )
    # stock: cantidad en inventario
    stock = fields.Integer(
        string='Stock',
        default=0,
    )
    # categ_id: categoría (Many2one a product.category)
    categ_id = fields.Many2one(
        'product.category',
        string='Categoría',
        required=True,
        ondelete='cascade',
    )
    # description: descripción libre
    description = fields.Text(
        string='Descripción',
    )