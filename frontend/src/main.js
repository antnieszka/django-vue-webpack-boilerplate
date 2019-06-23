import Vue from "vue";
import VueResource from "vue-resource";
import App from "./app";

Vue.config.devtools = true;
Vue.config.productionTip = false;

Vue.use(VueResource);

/* eslint-disable no-new */
new Vue({
  el: "#app",
  template: "<App/>",
  components: { App }
});
