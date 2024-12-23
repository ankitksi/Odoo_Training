/** @odoo-module **/
import { Component, useState } from "@odoo/owl";
import { View } from "@web/views/view";
import { Field } from "@web/views/fields/field";
import { Record } from "@web/model/record";
import { useService } from "@web/core/utils/hooks";
import { ViewScaleSelector } from "@web/views/view_components/view_scale_selector";
export class GridRenderer extends Component {
    async setup() {
        // Initialize necessary states
//        this.records = this.props.records;
        this.orm = useService("orm");
        this.records = useState(this.props.records);
        console.log(this.records);
    }

    async addRecord(ev) {
        ev.preventDefault(); // Prevent default form submission behavior

        const name = ev.target.querySelector("#name").value;
        const description = ev.target.querySelector("#description").value;

        if (!name || !description) {
            alert("Please fill out all fields!");
            return;
        }

        try {
            // Create a new record using ORM
            const newRecordId = await this.orm.create("custom.model", [{
                name,
                description,
            }]);
            this.records.push({
                id: newRecordId,
                name,
                description,
            });
            this.render();

            ev.target.reset();


            console.log("Record added successfully:", newRecordId);
        } catch (error) {
            console.error("Failed to add record:", error);
            alert("Error adding record. Check the console for details.");
        }
    }



}
GridRenderer.template = "grid_view.GridRenderer";
GridRenderer.components = {
    View,
    Field,
    Record,
    ViewScaleSelector,
};
