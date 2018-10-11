import login from './components/login.vue';
import cms from './components/cms.vue';
import impressum from './components/impressum.vue';

export default [
  { path: '/', component: login },
  { path: '/cms/:id', component: cms },
  { path: '/impressum', component: impressum }
]
