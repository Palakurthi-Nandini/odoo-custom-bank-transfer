{
    'name': 'Bank Transfer Payment Option',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Add NEFT/IMPS bank transfer payment option for website orders',
    'author': 'Your Name',
    'depends': ['website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/bank_transfer_form.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'payment_bank_transfer_custom/static/src/js/popup.js',
        ],
    },
    'installable': True,
    'application': True,
}