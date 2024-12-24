/** @odoo-module **/
import { Component, useState } from "@odoo/owl";
import { View } from "@web/views/view";
import { Field } from "@web/views/fields/field";
import { Record } from "@web/model/record";
import { useService } from "@web/core/utils/hooks";
import { _t } from "@web/core/l10n/translation";
import { ViewScaleSelector } from "@web/views/view_components/view_scale_selector";
export class GridRenderer extends Component {
    async setup() {
        // Initialize necessary states
//        this.records = this.props.records;
        this.orm = useService("orm");
        this.notification = useService("notification");
        this.records = useState(this.props.records);
        console.log(this.records);
    }

    async addRecord(ev) {
        ev.preventDefault(); // Prevent default form submission behavior

        const name = ev.target.querySelector("#name").value;
        const description = ev.target.querySelector("#description").value;

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

            this.notification.add(_t("Record added successfully"),
                                    {
                                    type:"success",
                                    title:_t("Success")
                                    })
            console.log("Record added successfully:", newRecordId);
        } catch (error) {
            this.notification.add(_t("Failed to add record"),
                        {
                        type:"danger",
                        title:_t("Failed")
                        })
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
