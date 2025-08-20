from odoo import models, fields, api

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
