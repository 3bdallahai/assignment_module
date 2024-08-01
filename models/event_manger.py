from odoo import fields, models, api, _

class EventManger(models.Model):
    _name= "event.manger"
    _description="Event manger"
    

    name = fields.Char(required=True)
    date = fields.Date(required=True)
    location= fields.Char(required=True)
    description= fields.Char()

  


