<template>
    <div style="width: 800px;margin: 0 auto">
        <div id="title"style="text-align: center">
        <h2 >
            这是用户列表页
        </h2>
        </div>

        <div id="add_user"style="text-align: center;margin-bottom: 10px" >
            <div style="display: block;overflow: auto">
            <input type="button"value="添加用户" @click="add_user"  style="float: right;margin-bottom: 10px">
            </div>
            <div id="add_user_content"v-show="add_user_show" >
                <table style="margin: 0 auto"border="0px"cellpadding="10px">
                    <tr style="margin-bottom: 10px">
                        <td style="text-align: right">姓 名:</td>
                        <td><input type="text" v-model="name"></td>
                    </tr>
                    <tr>
                        <td style="text-align: right">生 日:</td>
                        <td><input type="date" v-model="birthday"></td>
                    </tr>
                    <tr>
                        <td style="text-align: right">信 息:</td>
                        <td><input type="text" v-model="content"></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td><input type="button"value="提交"@click="submit_user"></td>
                    </tr>
                </table>
            </div>
        </div>

        <div id="user_list">
        <table border="0px" cellspacing="0px" cellpadding="0px" width="800px"  style="border-top: 10px;text-align: center;margin: 0 auto">
            <tr style="height: 50px">
                <td>id</td>
                <td>姓名</td>
                <td>生日</td>
                <td>个人信息</td>
                <td>操作</td>
            </tr>
            <tr v-for="(user,index) in users" :key="user.id" v-if="index%2==0" style="height: 50px;background-color:#f3f3f3">
                <td>{{ user.id }}</td>
                <td>{{ user.name }}</td>
                <td>{{ user.birthday }}</td>
                <td>{{ user.content }}</td>
                <td><a href="javascript:void(0)"@click="del_one(index)">删除</a> | <a href="javascript:void(0)"@click="detail(user.id)">查看详情</a></td>
            </tr>

            <tr v-else style="height: 50px;background-color: white">
                <td>{{ user.id }}</td>
                <td>{{ user.name }}</td>
                <td>{{ user.birthday }}</td>
                <td>{{ user.content }}</td>
                <td><a href="javascript:void(0)" @click="del_one(index)">删除</a> | <a href="javascript:void(0)"@click="detail(user.id)">查看详情</a></td>
            </tr>
        </table>
        </div>
    </div>
</template>

<script>
export default {
    name: "User",
    data(){
      return {
          users:[
              {'id':1,'name':'Tom','birthday':'1999-1-1','content':'来自山西太原'},
              {'id':2,'name':'Jack','birthday':'1999-5-1','content':'来自河北承德'},
              {'id':3,'name':'Linda','birthday':'1999-9-1','content':'来自北京'},
              {'id':4,'name':'Alice','birthday':'1999-6-1','content':'来自山西运城'},
          ],
          id:5,
          name:'',
          birthday:'',
          content:'',
          add_user_show:false,
      }
    },
    methods:{
        del_one(index){
            this.users.splice(index,1)
        },
        add_user(){
            this.add_user_show = !this.add_user_show
        },
        submit_user(){
            if (this.name&&this.name&&this.content){
                let a = {'id':this.id,'name':this.name,'birthday':this.birthday,'content':this.content}
                this.users.push(a)
                console.log(this.name,this.birthday,this.content)
                this.id ++
                this.name=''
                this.birthday=''
                this.content=''
            }
            else {
                alert('请检查输入')
            }
        },
        detail(id){
            this.$router.push({path:'/detail/'+id})
        },
    },
}
</script>

<style scoped>
a { text-decoration-line: none;
    color: black;
}
a:hover{
    color:cornflowerblue;
}
a:visited{
    color: #771caa;
}
#user_list td{
    border:1px solid grey;

}
</style>
