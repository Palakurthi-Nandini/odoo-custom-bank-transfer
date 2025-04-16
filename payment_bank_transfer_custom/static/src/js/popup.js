odoo.define('payment_bank_transfer_custom.popup', function (require) {
    "use strict";

    const publicWidget = require('web.public.widget');

    publicWidget.registry.BankTransferPopup = publicWidget.Widget.extend({
        selector: '.js_bank_transfer',
        events: {
            'click': '_onClick',
        },

        _onClick: function () {
            const orderTotal = $('.oe_cart .oe_total .oe_currency_value').text();
            $('#order_amount').text(orderTotal);
            $('#order_id').val($('.oe_website_sale').data('order-id'));
            $('#bank_transfer_modal').modal('show');
        },
    });
});