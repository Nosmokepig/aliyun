<template>
    <div id="app">

        <h2>
            欢迎您，这是页头
        </h2>

        <router-link to="/index">主页</router-link>
        <router-link to="/user">用户列表</router-link>
        <hr>
        <router-view></router-view>
    </div>
</template>

<script>

import Index from "./components/Index";
import User from "./components/User";
import Detail from "./components/Detail";

export default {
    name: 'App',
    components:{
        'Index':Index,
        'User':User,
        'Detail':Detail,
    }
}
</script>

<style>
</style>
