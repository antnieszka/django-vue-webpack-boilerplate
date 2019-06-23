import Vue from "vue";
import VueResource from "vue-resource";

import MainPageSearch from "./components/MainPageSearch";

Vue.config.devtools = true;
Vue.config.productionTip = false;

Vue.use(VueResource);

/* eslint-disable no-new */
new Vue({
  el: "#main-page-search",
  template: "<main-page-search/>",
  components: { MainPageSearch }
});
