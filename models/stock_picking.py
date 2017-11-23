# -*- coding: utf-8 -*-
# Copyright 2017 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import api, fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    env_user_is_stock_manager = fields.Boolean(
        string='Is a stock manager?',
        compute='_compute_is_stock_manager',
        search='_search_env_user_is_stock_manager')

    def _compute_is_stock_manager(self):
        """ Computes value of field env_user_is_stock_manager """

        for sp in self:
            sp.env_user_is_stock_manager = self.user_has_groups(
                'stock.group_stock_manager')

    def _search_env_user_is_stock_manager(self, operator, value):
        """ Computes the search operation in field env_user_is_stock_manager"""

        stock_picking_ids = list()
        env_user_is_stock_manager = self.user_has_groups(
            'stock.group_stock_manager')
        if env_user_is_stock_manager:
            stock_picking_ids = self.search([]).mapped('id')
        return [('id', 'in', stock_picking_ids)]
