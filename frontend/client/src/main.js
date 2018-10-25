import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Routes from './routes'
import VueResource from 'vue-resource'

Vue.config.productionTip = false

Vue.use(VueRouter);
Vue.use(VueResource);

const router = new VueRouter({
    routes: Routes
});

new Vue({
  render: h => h(App),
  router: router
}).$mount('#app')
