from odoo import models, fields

class CriteriaValues(models.Model):
    _name = 'my_module.criteria_values'
    _description = 'Valores de Criterio'
    _rec_name = 'name'

    name = fields.Selection(
        [
            ('confidencialidad', 'Confidencialidad'),
            ('integridad', 'Integridad'),
            ('disponibilidad', 'Disponibilidad'),
            ('probabilidad', 'Probabilidad'),
        ],
        string='Name',
        required=True,
    )
    criteria = fields.Char(
        string='Criteria',
        required=True,
    )
    value = fields.Char(
        string='Value',
        required=True,
    )
