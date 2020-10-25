import Vue from 'vue'
import Router from 'vue-router'
import Index from "../components/Index";
import User from "../components/User";
import Detail from "../components/Detail";

Vue.use(Router)

export default new Router({
  routes: [
    {path:'/index',component:Index},
    {path:'/user',component:User},
    {path:'/detail/:id',component:Detail},
    {path:'/',redirect:'/index'},
  ]
})
