from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_view_manufacturing_order(self):
        self.ensure_one()
        action = {
            'name': 'Manufacturing Orders',
            'type': 'ir.actions.act_window',
            'res_model': 'mrp.production',
            'view_mode': 'list,form',
            'domain': [('origin', '=', self.name)],
            'context': dict(self.env.context, default_origin=self.name)
        }
        list_view = self.env.ref('mrp.mrp_production_tree_view', False)
        form_view = self.env.ref('mrp.mrp_production_form_view', False)
        if list_view and form_view:
            action['views'] = [
                (list_view.id, 'list'),
                (form_view.id, 'form')
            ]
        return action

    def action_view_purchase_order(self):
        self.ensure_one()
        action = {
            'name': 'Purchase Orders',
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.order',
            'view_mode': 'list,form',
            'domain': [('origin', '=', self.name)],
            'context': dict(self.env.context, default_origin=self.name)
        }
        list_view = self.env.ref('purchase.purchase_order_tree', False)
        form_view = self.env.ref('purchase.purchase_order_form', False)
        if list_view and form_view:
            action['views'] = [
                (list_view.id, 'list'),
                (form_view.id, 'form')
            ]
        return action
