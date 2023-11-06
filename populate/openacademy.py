from odoo.tools import populate
from odoo.addons.base.populate.res_partner import Partner
from odoo import models


class Course(models.Model):
    _inherit = "openacademy.course"

    _populate_dependencies = ["res.users"]
    _populate_sizes = {"small": 100, "medium": 1000, "large": 10000}

    def _populate_factories(self):
        user_ids = self.env.registry.populated_models["res.users"]

        def get_name(value=None, counter=0, **kwargs):
            return "%s_%s" % ("course", counter)

        return [
            {
                "name": populate.compute(get_name),
                "responsible_id": populate.randomize(user_ids)
            }
        ]
