import DS from 'ember-data';

export default DS.Model.extend({

    parameters: DS.hasMany('parameter', {
        inverse: 'cases',
        async: true
    }),
    values: DS.hasMany('value', {
        inverse: 'caxe',
        async: true
    }),
    workflow: DS.belongsTo('workflow', {
        inverse: 'cases',
        async: true
    }),
    initialState: DS.attr(),
    messages: DS.hasMany('message', {
        inverse: 'caxe',
        async: true
    }),

});

