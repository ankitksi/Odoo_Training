/** @odoo-module **/

import { Dialog } from "@web/core/dialog/dialog";
import { registry } from "@web/core/registry";

export class CustomDialogAction {
    /**
     * Entry point for the client action.
     * @param {Object} env - The environment context.
     * @param {Object} options - The options passed to the action.
     */
    setup(env, options) {
        this.env = env;
        this.options = options || {};
    }

    async start() {
        new Dialog(this, {
            title: this.options.title || "Custom Dialog",
            body: this.options.body || "This is a custom dialog opened using client action!",
            buttons: [
                {
                    text: "Close",
                    classes: "btn-primary",
                    close: true,
                },
            ],
        }).open();
    }
}

registry.category("actions").add("custom_dialog_action", CustomDialogAction);
