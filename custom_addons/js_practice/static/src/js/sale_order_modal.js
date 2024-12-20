odoo.define('your_module.sale_order_modal', function (require) {
    "use strict";

    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var QWeb = core.qweb;
    var rpc = require('web.rpc');

    var SaleOrderModal = AbstractAction.extend({
        template: 'SaleOrderModalTemplate',

        events: {
            'click .close-modal': 'close_modal',
        },

        init: function (parent, action) {
            this._super(parent, action);
        },

        start: function () {
            var self = this;
            // Optional: You can make an RPC call to fetch some data here
            return this._super.apply(this, arguments).then(function () {
                // Additional logic for modal if needed
            });
        },

        close_modal: function () {
            this.do_action({type: 'ir.actions.client', tag: 'close'});
        },
    });

    core.action_registry.add('sale_order_modal_action', SaleOrderModal);
});
