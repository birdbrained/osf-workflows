import Ember from 'ember';
/* global Freewall */
//import 'bower_components/freewall/freewall';
//
export default Ember.Route.extend({

    model: function(params, transition, queryParams) {
        //return this.get('store').query('message', {
            //filter: {
                return this.modelFor('cases.case').get('messages')
            //}
        //});
    },

    setupController: function(controller, model) {
        controller.set('messages', model)
    }

});
