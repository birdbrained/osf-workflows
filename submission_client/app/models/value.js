import DS from 'ember-data';

export default DS.Model.extend({

    color: DS.attr(),
    caxe: DS.belongsTo('case', {
        inverse: 'values',
        async: true
    }),
    parameter: DS.belongsTo('parameter', {
        inverse: 'values',
        async: true,
    }),
    state: DS.attr('string'),
    value: DS.attr()

});

