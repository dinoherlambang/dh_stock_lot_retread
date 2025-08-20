{
    'name': 'Stock Lot Retread',
    'version': '13.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Add Retread field to stock.production.lot',
    'author': 'Dino Herlambang',
    'depends': ['stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_production_lot_views.xml',
    ],
    'installable': True,
}
