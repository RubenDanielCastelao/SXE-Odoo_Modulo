# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'
#     _description = 'openacademy.openacademy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import fields, models

class materiales(models.Model):
    _name = 'materiales'
    _description = 'tabla de materiales y sus datos'

    name = fields.Char(String = 'Nombre')
    description = fields.Char(String = 'Descripcion')
    precio = fields.Float(String = 'Precio')