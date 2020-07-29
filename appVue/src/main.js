// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from "./vuex/store";
import ElementUi from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Axios from 'axios'
import VueCodemirror from 'vue-codemirror'
import 'codemirror/lib/codemirror.css'

Vue.config.productionTip = false
Vue.use(ElementUi)
Vue.prototype.$http = Axios //全局使用axios
Vue.use(VueCodemirror)
Axios.defaults.headers.post['Content-Type'] = 'application/x-www-fromurlencodeed'///配置请求头，非常重要，有了这个才可以正常使用POST等请求后台数据
Vue.prototype.$url = 'http://10.123.193.24:8000/api'

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
