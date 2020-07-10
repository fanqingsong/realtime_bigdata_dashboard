import Vue from 'vue'
import Router from 'vue-router'
import WordCloud from '@/components/WordCloud'

Vue.use(Router)

export default new Router({
    routes: [{
        path: '/',
        name: 'WordCloud',
        component: WordCloud
    }]
})