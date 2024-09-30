odoo.define('cd_recipe_material_management.pos_cart_validation', function (require) {
    "use strict";

    const PosModel = require('point_of_sale.models');
    const PosScreen =   require('point_of_sale.screens');

    // Extend the existing PosModel to include our validation logic
    const _super_order = PosModel.Order.prototype;

    PosModel.Order = PosModel.Order.extend({
        initialize: function (attributes) {
            _super_order.initialize.apply(this, arguments);
        },

        // Override the 'export_as_JSON' method to add custom validations
        export_as_JSON: function () {
            const json = _super_order.export_as_JSON.call(this);

            // Add your validation logic here
            if (this.get_orderlines().length === 0) {
                throw new Error("You cannot check out with an empty cart.");
            }

            // Example validation: Check if all products have a quantity greater than zero
            for (const line of this.get_orderlines()) {
                if (line.get_quantity() <= 0) {
                    throw new Error("All products must have a quantity greater than zero.");
                }
            }

            return json;
        },
    });

    // Extend the PosScreen to show validation messages
    PosScreen.OrderWidget.include({
        validate_order: function () {
            try {
                this._super();
                // If validation passes, proceed with the order
            } catch (error) {
                // Show an error message to the user
                this.gui.show_popup('error', {
                    title: 'Validation Error',
                    body: error.message,
                });
            }
        },
    });
});
