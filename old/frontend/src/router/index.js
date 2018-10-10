import Vue from 'vue'
import Router from 'vue-router'
import VueRouter from 'vue-router'
import login from '@/components/login'
import main from '@/components/mainPage'
import personalInformation from '@/components/personalInformation'
import personalPosts from '@/components/personalPosts'

// Vue.use(Router)
//
// export default new Router({
//   routes: [
//     {
//       path: '/',
//       name: 'HelloWorld',
//       component: HelloWorld
//     }
//   ]
// })




Vue.use(VueRouter)

export default new VueRouter({
//const router = new VueRouter({
  routes: [
    {
      path: '/',
      //name: 'login',
      component: login
    },
    {
      path: '/mainPage',
      //name: 'mainPage',
      component: main
      // meta: {
      //   requiresAuth: true
      // }
    },
    {
      path: '/personalInformation',
      //name: 'mainPage',
      component: personalInformation
      // meta: {
      //   requiresAuth: true
      // }
    },
    {
      path: '/personalPosts',
      //name: 'mainPage',
      component: personalPosts
      // meta: {
      //   requiresAuth: true
      // }
    }
  ],
});



// router.beforeEach((to, from, next) => {
//   if (to.meta.requiresAuth && true) {
//     next('/');
//   } else {
//     next();
//   }
// });
