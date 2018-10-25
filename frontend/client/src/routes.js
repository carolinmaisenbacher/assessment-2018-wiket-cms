import login from './components/login.vue';
import cms from './components/cms.vue';
import impressum from './components/impressum.vue';
import home from './components/home.vue';
// import cmsWhere from './components/cms/cmsWhere.vue';
// import cmsWhen from './components/cms/cmsWhen.vue';
import cmsMenu from './components/cms/cmsMenu.vue';
// import cmsIntro from './components/cms/cmsIntro.vue';
// import cmsWe from './components/cms/cmsWe.vue';

export default [
  { path: '/', component: login },
  { path: '/cms/:id', component: cms, props: true },
  { path: '/impressum', component: impressum },
  { path: '/home', component: home },
  // { path: '/cms/where', component: cmsWhere },
  // { path: '/cms/when', component: cmsWhen },
  { path: '/cmsMenu', component: cmsMenu },
  // { path: '/cms/intro', component: cmsIntro },
  // { path: '/cms/we', component: cmsWe },
]
