import Vue from 'vue'
import Router from 'vue-router'
import Homepage from '@/components/Homepage'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: __dirname,
  routes: [
    {
      name: 'Homepage',
      path: '/home',
      component: Homepage
    },{
      name: 'Analysis',
      path: '/analysis',
      component: ()=>import('@/views/CodeHub/analysis.vue')
    },{
      name: 'CodeHub',
      path: '/codehub',
      component: ()=>import('@/views/CodeHub/document.vue')
    },{
      name: 'Admin',
      path: '/admin',
      component:()=>import(this.$url+'/admin')
    },{
      name: 'CodeRelease',
      path: '/coderelease',
      component:()=>import('@/views/CodeRelease/version.vue')
    }
  ]
})
