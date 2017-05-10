import DS from 'ember-data';

export default DS.Model.extend({

    name: DS.attr('string'),
    description: DS.attr('string'),
    group: DS.belongsTo('group', {
        async: true
    }),
    action_function: DS.attr('string'),
    output: DS.belongsTo('parameter', {
        async: true
    }),
    conditions: DS.hasMany('condition', {
        inverse: 'action',
        async: true
    }),
    messages: DS.hasMany('message', {
        inverse: 'origin',
        async: true
    })

});

