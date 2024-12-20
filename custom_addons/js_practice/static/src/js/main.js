/** @odoo-module */

import { registry } from "@web/core/registry";
import { IncrementButton } from "./index";

registry.category("actions").add("increment_button_action", IncrementButton);
