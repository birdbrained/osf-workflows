import DS from 'ember-data';

export default DS.Model.extend({

    messageType: DS.attr('string'),
    timestamp: DS.attr('date'),
    view: DS.attr('string'),
    caxe: DS.belongsTo('case', {
        inverse: 'messages',
        async: true
    }),
    origin: DS.hasMany('action', {
        inverse: 'messages',
        async: true
    }),
    response: DS.belongsTo('parameter', {
        inverse: "messages",
        async: true
    }),
    content: DS.attr('string'),
    section: DS.attr('string'),

});

