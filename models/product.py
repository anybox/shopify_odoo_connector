from openerp import models, fields


class product_template(models.Model):
    _inherit = 'product.template'

    state = fields.Selection([('draft', 'Draft'), ('add', 'Add To Shopify'),
                              ('update', 'Update To Shopify')], "Status", default='draft')
    shopify_product_id = fields.Char('Shopify Product')


class product_product(models.Model):
    _inherit = 'product.product'

    product_sfy_variant_id = fields.Char("Shopify Product Variant")


class product_category(models.Model):
    _inherit = 'product.category'

    description = fields.Text('Description')
    shopify_product_cate_id = fields.Char('Shopify Product Category')
