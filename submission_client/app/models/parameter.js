import DS from 'ember-data';

export default DS.Model.extend({

    name: DS.attr('string'),
    view: DS.attr('string'),
    cases: DS.hasMany('cases', {
        inverse: 'parameters',
        async: true
    }),
    values: DS.hasMany('value', {
        inverse: 'parameter',
        async: true,
    }),
    sources: DS.hasMany('action', {
        inverse: 'output',
        async: true
    }),
    messages: DS.hasMany('message', {
        inverse: 'response',
        async: true
    }),
    conditions: DS.hasMany('condition', {
        inverse: 'parameter',
        async: true
    })

});

