# Copyright 2020 ForgeFlow S.L. (http://www.forgeflow.com)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)

import logging

from odoo import models, api

_logger = logging.getLogger(__name__)


class Base(models.AbstractModel):
    _inherit = 'base'

    @api.multi
    def with_delay(self, priority=None, eta=None,
                   max_retries=None, description=None,
                   channel=None, identity_key=None):
        return super(
            Base, self.with_context(test_queue_job_no_delay=True)).with_delay(
            priority=priority, eta=eta, max_retries=max_retries,
            description=description, channel=channel, identity_key=identity_key)
