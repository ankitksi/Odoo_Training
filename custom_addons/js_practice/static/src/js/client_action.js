/** @odoo-module **/
//js_practice/static/src/js/client_action.js
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { useState } from "@odoo/owl";

const { Component } = owl;

export class AdvancedDashboard extends Component {
    setup() {
        // Use necessary services
        this.action = useService("action");
        this.rpc = this.env.services.rpc;

        // Initialize state to hold dashboard data
        this.state = useState({
            data: [],
        });

        // Load data when the component is mounted
        this.loadData();
    }

    async loadData() {
        try {
            // Fetch data from the backend using RPC
            const data = await this.rpc.query({
                model: "partner.dashboard",
                method: "get_values",
                args: [],
            });
            console.log("Fetched Data:", data);

            // Update the component's state
            this.state.data = data;
        } catch (error) {
            console.error("Error fetching dashboard data:", error);
        }
    }
}

// Define the template for the component
AdvancedDashboard.template = "client_action.advanced_dashboard";

// Register the client action
registry.category("actions").add("advanced_dashboard", AdvancedDashboard);
