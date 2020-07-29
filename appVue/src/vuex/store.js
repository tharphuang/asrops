//引入vue及vuex
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

//需要维护的状态
const state = {
    notes:[],
    activeNote:{}
}

const mutations = {

}

const actions = {

}
const getters = {

}

export default new Vuex.Store({
    state,
    mutations,
    actions,
    getters
})
