from odoo import models, fields, api

class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    retread = fields.Boolean(string='Retread (Vulkanisir)')
    pl_type = fields.Char(string='PL Type', help='Production Lot Type')
    tire_size = fields.Char(string='Tire Size', help='Size specification of the tire')
    
    # Add default owner field (safer approach)
    default_owner_id = fields.Many2one(
        'res.partner', 'Default Owner',
        help='Default owner for this lot/serial number. Actual ownership is tracked per location in stock quants.',
        check_company=True
    )
    
    # Computed field to show current actual owner(s) from quants
    current_owner_ids = fields.Many2many(
        'res.partner', 
        compute='_compute_current_owners',
        string='Current Owners',
        help='Current actual owners based on stock quants in different locations'
    )
    
    @api.depends('quant_ids.owner_id')
    def _compute_current_owners(self):
        """Compute current owners from existing quants"""
        for lot in self:
            owners = lot.quant_ids.mapped('owner_id')
            lot.current_owner_ids = owners
    
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
