<template>
    <div>
        <h3>这是用户详情页</h3>
        该用户的id为 ：{{$route.params.id}}
        <br>
        <input type="button"value="返回"@click="back">
    </div>
</template>

<script>
export default {
    name: "Detail",
    methods:{
      back(){
       this.$router.go(-1)
      }
    },
}
</script>

<style scoped>

</style>
