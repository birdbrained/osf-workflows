import Ember from 'ember';
/* global Freewall */
//import 'bower_components/freewall/freewall';
//
export default Ember.Route.extend({

    model: function() {
        return {
            messages: this.modelFor('cases.case.inbox'),
            caxe: this.modelFor('cases.case')
        }
    },

    setupController: function(controller, model) {
        controller.set('messages', model.messages);
        controller.set('caxe', model.caxe);
    }

});
