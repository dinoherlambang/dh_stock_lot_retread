# Stock Lot Retread Module

## Overview

This Odoo module extends the stock production lot functionality by adding retread and tire-specific fields.

## Features

- Adds a Boolean field for retread (vulkanisir) tracking
- Adds PL Type field for Production Lot Type specification  
- Adds Tire Size field for tire size specification
- Conditional Product Requirement: Product field becomes optional when retread is checked
- Smart Validation: Product field is mandatory only when retread is False
- Integrated into both form and tree views
- Proper access rights configuration

## Module Information

- Name: Stock Lot Retread
- Technical Name: dh_stock_lot_retread
- Version: 13.0.1.0.0
- Category: Inventory
- Author: Dino Herlambang
- Depends: stock

## Installation

1. Copy the module to your Odoo addons directory
2. Update the module list in Odoo
3. Install the module from the Apps menu

## Safety Analysis

This module has been thoroughly analyzed for safety and compatibility:

### Field Overriding
- Override product_id with required=False
- Base field has required=True, our override is valid
- Keep check_company=True (security maintained)
- Domain is inherited from base (functionality preserved)

### Constraint Validation
- api.constrains properly declared
- Constraint checks both product_id and retread fields
- ValidationError is proper Odoo exception
- Logic: product required only when retread=False

### View Inheritance
- XPath targets existing fields (product_id, ref)
- Uses position="attributes" for safe attribute modification
- attrs syntax is correct for conditional requirements
- No conflicts with base view structure

### Module Structure
- Proper __init__.py imports
- __manifest__.py has correct dependencies
- Security file has proper access rights
- No circular dependencies
- Follows Odoo development best practices

## Usage

### Form View
The module adds three new fields after the Internal Reference field:
- Retread (Vulkanisir): Boolean checkbox
- PL Type: Text field for production lot type
- Tire Size: Text field for tire size specification

When retread is unchecked: Product field is mandatory (red label)
When retread is checked: Product field becomes optional (normal label)

### Tree View
All new fields are available as optional columns in the list view.

## Technical Details

### New Fields
- retread: Boolean field with string 'Retread (Vulkanisir)'
- pl_type: Char field with string 'PL Type'
- tire_size: Char field with string 'Tire Size'

### Product Field Override
The product_id field is overridden to be conditionally required based on the retread field value.

### Validation
Custom constraint ensures product_id is required when retread is False.

### Views
- Form view: Inherits stock.view_production_lot_form
- Tree view: Inherits stock.view_production_lot_tree
- Uses XPath positioning for safe inheritance

## File Structure

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

## Changelog

### Version 13.0.1.0.0
- Initial release
- Added retread Boolean field
- Added pl_type and tire_size Char fields
- Conditional product requirement implementation
- Form and tree view integration
- Custom validation with constrains method
- Access rights configuration

## Safety Analysis

This section documents the safety considerations and implementation details.

### Field Overriding
- We override product_id with required=False
- Base field has required=True, our override is valid
- We keep check_company=True (security maintained)
- Domain is inherited from base (functionality preserved)

### Constraint Validation
- @api.constrains properly declared
- Constraint checks both product_id and retread fields
- ValidationError is proper Odoo exception
- Logic: product required only when retread=False

### View Inheritance
- XPath targets existing fields (product_id, ref)
- Uses position="attributes" for safe attribute modification
- attrs syntax is correct: required when retread equals False
- No breaking changes to existing views

### Module Structure
- Proper __init__.py imports
- __manifest__.py has correct dependencies
- Security file has proper access rights
- No circular dependencies
- Follows Odoo best practices

## License

This module is provided for internal use.
