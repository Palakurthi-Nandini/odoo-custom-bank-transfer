from odoo import models, fields

class BankTransferPayment(models.Model):
    _name = 'bank.transfer.payment'
    _description = 'Bank Transfer Payment Details'

    order_id = fields.Many2one('sale.order', string="Order")
    customer_id = fields.Many2one('res.partner', string="Customer")
    transfer_reference = fields.Char(string="Transfer Reference Number")
    screenshot = fields.Binary(string="Transaction Screenshot")
    comment = fields.Text(string="Additional Comments")