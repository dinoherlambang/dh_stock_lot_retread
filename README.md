# Stock Lot Retread Module

## Overview

This Odoo module extends the stock production lot functionality by adding a retread (vulkanisir) field to track whether a tire or product has been retreaded.

## Features

- Adds a Boolean field `retread` to the `stock.production.lot` model
- Adds a Char field `pl_type` for Production Lot Type specification
- Adds a Char field `tire_size` for tire size specification
- Field is displayed with the label "Retread (Vulkanisir)"
- Integrated into both form and tree views of stock production lots
- **Conditional Product Requirement**: When the retread field is checked (True), the Product field becomes optional
- **Smart Validation**: Product field is mandatory only when retread is False, allowing flexibility for retreaded items
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


## SAFETY ANALYSIS 

1. FIELD OVERRIDING:
   ✓ We override product_id with required=False
   ✓ Base field has required=True, our override is valid
   ✓ We keep check_company=True (security maintained)
   ✓ Domain is inherited from base (functionality preserved)

2. CONSTRAINT VALIDATION:
   ✓ @api.constrains properly declared
   ✓ Constraint checks both product_id and retread fields
   ✓ ValidationError is proper Odoo exception
   ✓ Logic: product required only when retread=False

3. VIEW INHERITANCE:
   ✓ XPath targets existing fields (product_id, ref)
   ✓ Uses position="attributes" for safe attribute modification
   ✓ attrs syntax is correct: {'required': [('retread', '=', False)]}

4. MODULE STRUCTURE:
   ✓ Proper __init__.py imports
   ✓ __manifest__.py has correct dependencies
   ✓ Security file has proper access rights
   ✓ No circular dependencies

## Usage

### Form View
When viewing or editing a stock production lot record, you will see the "Retread (Vulkanisir)" checkbox field after the Internal Reference field.

**Conditional Product Requirement**:
- When retread is **unchecked (False)**: Product field is **mandatory** (red label)
- When retread is **checked (True)**: Product field becomes **optional** (normal label)

This allows you to create lot records for retreaded items without requiring a specific product association.

### Tree View
In the list view of stock production lots, the retread field is available as an optional column that can be toggled on/off using the column selection options.

## Technical Details

### Model Extension
```python
class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    retread = fields.Boolean(string='Retread (Vulkanisir)')
    pl_type = fields.Char(string='PL Type', help='Production Lot Type')
    tire_size = fields.Char(string='Tire Size', help='Size specification of the tire')
    
    # Override product_id to make it conditionally required
    product_id = fields.Many2one(
        'product.product', 'Product',
        required=False,  # Remove the base required=True
        check_company=True
    )
    
    @api.constrains('product_id', 'retread')
    def _check_product_required(self):
        """Validate that product_id is required when retread is False"""
        for record in self:
            if not record.retread and not record.product_id:
                raise models.ValidationError(
                    "Product is required when the lot is not marked as retread."
                )
```

### View Inheritance
- **Form View**: Inherits `stock.view_production_lot_form`
  - Adds retread field after Internal Reference
  - Makes product field conditionally required with `attrs={'required': [('retread', '=', False)]}`
- **Tree View**: Inherits `stock.view_production_lot_tree`
  - Adds retread field as optional column

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
- **Conditional product requirement**: Product field is optional when retread is True
- Smart validation with custom constrains method
- Access rights configuration

## Support

For issues or questions regarding this module, please contact the module author.

## License

This module is provided as-is for internal use.
