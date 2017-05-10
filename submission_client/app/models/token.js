import DS from 'ember-data';

export default DS.Model.extend({

    color: DS.attr(),
    caxe: DS.belongsTo('case', {
        inverse: "tokens",
        async: true
    }),
    location: DS.belongsTo('location', {
        inverse: "tokens",
        async: true
    }),
    name: DS.attr('string'),
    requestMessages: DS.hasMany("message", {
        inverse: "responseTokens",
        async: true
    }),
    net: DS.belongsTo('net')

});

