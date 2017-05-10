
import Ember from 'ember';
import ENV from 'analytics-dashboard/config/environment';

function getToken() {
    const session = window.localStorage['ember_simple_auth:session'];
    if (session) {
        const token = JSON.parse(session)['authenticated'];
        if ('attributes' in token) {
            return token['attributes']['accessToken'];
        }
        return token;
    }
}

export default Ember.Component.extend({

    actions: {

        uploadFile: async function(target) {
            const reader = new FileReader();
            const f = event.target.files[0];
            const uri = "https://files.osf.io/v1/resources/h8d72/providers/osfstorage/?kind=file&name=" + f.name;
            const message = this.get('message');
            const parameter = this.get('message.response');
            const caxe = this.get('message.caxe');
            this.get('store').findRecord('case', this.get('message.caxe.id')).then((caxeo)=>{

                const refresh = this.attrs.refresh;
                const store = this.get("store");

                reader.onloadend = function(e) {
                    const xhr = new XMLHttpRequest();
                    xhr.open("PUT", uri, true);
                    xhr.setRequestHeader("Authorization", "Bearer " + getToken());
                    xhr.withCredentials = false;
                    xhr.onreadystatechange = async function() {
                        if (xhr.readyState == 4 && xhr.status >= 200 && xhr.status < 300) {
                            const value = store.createRecord('value');
                            value.set('value', JSON.parse(xhr.responseText).data.links.download);
                            value.set('caxe', caxe);
                            value.set('state', 'defined');
                            value.set('parameter', parameter);
                            await value.save();
                            refresh();
                        }
                    };
                    xhr.send(e.target.result);
                };
            })

            reader.readAsBinaryString(f);
        },

        associateResource: async function(resourceIdentifier) {
        }

    }

});
