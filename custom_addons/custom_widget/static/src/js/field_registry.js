/** @odoo-module **/

import { registry } from "@web/core/registry";
import { ExpressionWidget } from "./expression_widget";

registry.category("fields").add("expression_widget", ExpressionWidget);
