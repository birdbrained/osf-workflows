import DS from 'ember-data';

export default DS.Model.extend({

    parameter: DS.belongsTo('parameter', {
        inverse: 'conditions',
        async: true
    }),
    state: DS.attr('string'),
    type: DS.attr('string'),
    action: DS.belongsTo('action', {
        inverse: 'conditions',
        async: true
    }),
    workflow: DS.belongsTo('workflow', {
        inverse: 'conditions',
        async: true
    })

});

