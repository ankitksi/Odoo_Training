/** @odoo-module **/

import { Dialog } from "@web/core/dialog/dialog";
import { registry } from "@web/core/registry";

const { Component } = owl;

class CustomDialogAction extends Component {
    setup() {
        this.openDialog = this.openDialog.bind(this);
    }

    openDialog() {
        new Dialog(this, {
            title: "Custom Dialog",
            size: "medium",
            buttons: [
                { text: "Close", close: true, classes: "btn-primary" },
            ],
            $content: $("<div>", {
                text: "This is a custom dialog opened using a client action!",
            }),
        }).open();
    }
}

CustomDialogAction.template = "custom_dialog_action";

registry.category("actions").add("custom_dialog.action", CustomDialogAction);
export default CustomDialogAction;
