/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";
import { useState } from "@odoo/owl";

class ToggleSwitchWidget extends Component {
    setup() {
        console.log(this.props.record.data.toggle_state);
        this.state = useState({
            displayMode: this.props.readonly ? "readonly" : "edit",
            toggleState: this.props.record.data[this.props.name] || "off", // Initial state as string
        });

        this.toggleOptions = ["on","off", "intermediate"]; // Define possible states
    }

    async toggleState() {
        // Cycle through the toggle options
        const currentIndex = this.toggleOptions.indexOf(this.state.toggleState);
        this.state.toggleState = this.toggleOptions[(currentIndex + 1) % this.toggleOptions.length];

        // Save the updated state to the database
        try {
            await this.props.record.update({
                toggle_state: this.state.toggleState,
            });
        } catch (error) {
            console.error("Error updating toggle state in database:", error);
        }
    }
}

ToggleSwitchWidget.template = "widget_expression.ToggleSwitchWidget";
export const widgetToggleSwitchField = {
    component: ToggleSwitchWidget,
    supportedTypes: ["Char"], // Adjust to your field type
};

registry.category("fields").add("widget_toggle_switch", widgetToggleSwitchField);