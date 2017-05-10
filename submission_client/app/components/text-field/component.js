import Ember from 'ember';
import ENV from 'analytics-dashboard/config/environment';


export default Ember.Component.extend({

    preprintTitleObserver: Ember.observer('preprintTitle', async function() {

        const message = this.get('message');
        const parameter = this.get('message.response');
        const caxe = this.get('message.caxe');

        this.get('store').findRecord('case', this.get('message.caxe.id')).then(async (caxeo)=>{

            const refresh = this.attrs.refresh;
            const store = this.get("store");
            const value = store.createRecord('value');
            value.set('value', this.get('preprintTitle'));
            value.set('caxe', caxe);
            value.set('state', 'defined');
            value.set('parameter', parameter);
            const response = await value.save();
            this.get('store').findAll('message', {reload: true}).then((messages) => {
                this.attrs.refresh()
            })
            //refresh();

        })

    }),

});
