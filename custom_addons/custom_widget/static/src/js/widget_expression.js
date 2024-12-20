/** @odoo-module **/

import { Field } from "@web/views/fields/field";
import { Widget } from "@web/views/widgets/widget";

export class ExpressionWidget extends Widget {
    setup() {
        super.setup();
        this.isEditMode = this.props.mode === "edit";
        this.expression = this.props.value || "";
        this.result = this.evaluateExpression(this.expression);
    }

    evaluateExpression(expression) {
        try {
            // Evaluate the mathematical expression safely
            return eval(expression);
        } catch (error) {
            return "Invalid Expression";
        }
    }

    onInputChange(event) {
        const newValue = event.target.value;
        this.trigger("update", { value: newValue });
    }

    render() {
        if (this.isEditMode) {
            this.el.innerHTML = `<input type="text" value="${this.expression}" class="o_field_char" />`;
            this.el.querySelector("input").addEventListener("input", (e) => this.onInputChange(e));
        } else {
            this.el.innerHTML = `<span>${this.result}</span>`;
        }
    }
}
