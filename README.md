# Stock Lot Retread Module

## Overview

This Odoo module extends the stock production lot functionality by adding a retread (vulkanisir) field to track whether a tire or product has been retreaded.

## Features

- Adds a Boolean field `retread` to the `stock.production.lot` model
- Field is displayed with the label "Retread (Vulkanisir)"
- Integrated into both form and tree views of stock production lots
- Proper access rights configuration for different user groups

## Module Information

- **Name**: Stock Lot Retread
- **Technical Name**: `dh_stock_lot_retread`
- **Version**: 13.0.1.0.0
- **Category**: Inventory
- **Author**: Dino Herlambang
- **Depends**: stock

## Installation

1. Copy the module to your Odoo addons directory
2. Update the module list in Odoo
3. Install the module from the Apps menu

## Usage

### Form View
When viewing or editing a stock production lot record, you will see the "Retread (Vulkanisir)" checkbox field after the Internal Reference field.

### Tree View
In the list view of stock production lots, the retread field is available as an optional column that can be toggled on/off using the column selection options.

## Technical Details

### Model Extension
```python
class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    retread = fields.Boolean(string='Retread (Vulkanisir)')
```

### View Inheritance
- **Form View**: Inherits `stock.view_production_lot_form`
- **Tree View**: Inherits `stock.view_production_lot_tree`

### Access Rights
- **Base Users**: Read-only access to the retread field
- **Stock Managers**: Full access (read, write, create, unlink)

## File Structure

```
dh_stock_lot_retread/
├── __init__.py
├── __manifest__.py
├── README.md
├── models/
│   ├── __init__.py
│   └── stock_production_lot.py
├── security/
│   └── ir.model.access.csv
└── views/
    └── stock_production_lot_views.xml
```

## Changelog

### Version 13.0.1.0.0
- Initial release
- Added retread Boolean field to stock.production.lot
- Form and tree view integration
- Access rights configuration

## Support

For issues or questions regarding this module, please contact the module author.

## License

This module is provided as-is for internal use.
