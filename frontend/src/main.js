// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Login from './Login'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'



Vue.use(BootstrapVue);

Vue.config.productionTip = false

/* eslint-disable no-new */

var main = new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

var login = new Vue({
  el: '#login',
  components: { Login },
  template: '<Login/>'
})
