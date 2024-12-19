/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";
import { useState } from "@odoo/owl";

class ExpressionWidget extends Component {
    setup() {
        // Initial state
        this.state = useState({
            expression: this.props.record.data[this.props.name] || "", // Current expression
            displayMode: this.props.readonly ? "readonly" : "edit", // Display mode
            result: "", // Evaluated result
        });

        this.evaluateExpression();
    }

    evaluateExpression() {
        try {
            // Replace `eval` with safe evaluation logic or a custom parser
            this.state.result = eval(this.state.expression); // CAUTION: Avoid eval in production.
        } catch (error) {
            console.error("Error evaluating expression:", error);
            this.state.result = "Invalid Expression";
        }
    }

    async updateExpression(event) {
        // Update the expression in state
        this.state.expression = event.target.value;

        // Reevaluate the expression
        this.evaluateExpression();

        // Save the updated expression in the database
        try {
            await this.props.record.update({
                expression: this.state.expression, // Update the expression field
            });
        } catch (error) {
            console.error("Error updating expression in database:", error);
        }
    }
}

ExpressionWidget.template = "widget_expression.ExpressionWidget";

// Register the widget for Char fields
export const widgetExpressionField = {
    component: ExpressionWidget,
    supportedTypes: ["Char"],
};

registry.category("fields").add("widget_expression", widgetExpressionField);
