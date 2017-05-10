import DS from 'ember-data';

export default DS.Model.extend({

    name: DS.attr('string'),
    description: DS.attr('string'),
    group: DS.belongsTo("group"),
    transitions: DS.hasMany('transition', {
        inverse: 'net',
        async: true
    }),
    locations: DS.hasMany('location', {
        inverse: 'net',
        async: true
    }),
    cases: DS.hasMany("case")

});

