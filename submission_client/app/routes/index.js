import Ember from 'ember';
/* global Freewall */
//import 'bower_components/freewall/freewall';
//
export default Ember.Route.extend({

    model() {
        return this.get('store').findRecord("workflow", "c4a2a604-aa56-444b-a450-ef17be5f7e38");
    },

    setupController: async function(controller, model) {
        controller.set("workflow", model);
        console.log(model)
    }

});
