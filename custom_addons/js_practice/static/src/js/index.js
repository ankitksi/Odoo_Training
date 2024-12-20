/** @odoo-module */

import { Component, useState } from "@odoo/owl";

export class IncrementButton extends Component {
    // Template reference
    static template = "js_practice.IncrementButtonTemplate";

    // Component logic
    setup() {
        // Reactive state with an initial value of 0
        this.state = useState({ count: 0 });
    }

    // Function to increment the value
    increment() {
        this.state.count += 1;
    }
}
