/** @odoo-module **/

import { registry } from "@web/core/registry";
import { ExpressionWidget } from "./widget_expression";

registry.category("fields").add("expression_widget", ExpressionWidget);
