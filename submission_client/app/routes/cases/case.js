import Ember from 'ember';
/* global Freewall */
//import 'bower_components/freewall/freewall';
//
export default Ember.Route.extend({

    model: function(params, transition, queryParams) {
        return this.get('store').findRecord('case', params.case, {reload: true});
    },

    setupController: function(controller, model) {
        controller.set('caxe', model)
    }


});
