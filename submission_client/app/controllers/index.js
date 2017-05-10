import Ember from "ember";

export default Ember.Controller.extend({

    actions: {

        beginWorkflow: async function(workflow) {
            let wfcase = this.get('store').createRecord('case');
            wfcase.set("workflow", workflow)
            await wfcase.save();
            this.transitionToRoute('cases.case.inbox', wfcase.id)
        }

    }

});
