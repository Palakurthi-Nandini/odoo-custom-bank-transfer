from odoo import http
from odoo.http import request

class BankTransferController(http.Controller):

    @http.route('/bank_transfer/submit', type='http', auth="user", website=True)
    def submit_bank_transfer(self, **kwargs):
        request.env['bank.transfer.payment'].sudo().create({
            'order_id': int(kwargs.get('order_id')),
            'customer_id': request.env.user.partner_id.id,
            'transfer_reference': kwargs.get('transfer_reference'),
            'screenshot': kwargs.get('screenshot'),
            'comment': kwargs.get('comment'),
        })
        return request.redirect('/shop/confirmation')