<template>
    <div class="footer">
        <ul>
            <li v-for="(footer,index) in footer_list":key="index"><a :href="footer.link" class="footer_text">{{footer.title}}</a></li>
        </ul>
    </div>
</template>

<script>
export default {
    name: "Footer",
    data(){
        return {
            footer_list : [],
        }
    },
    methods:{
        get_all_footer(){
            this.$axios.get(this.$settings.HOST+'home/footer/').then(response=>{
                this.footer_list = response.data
            })
        },
    },
    created() {
        this.get_all_footer();
    }
}
</script>

<style scoped>
.footer {
    width: 100%;
    height: 128px;
    background: #25292e;
    color: #fff;
}

.footer ul {
    margin: 0 auto 16px;
    padding-top: 38px;
    width: 810px;
}

.footer ul li {
    float: left;
    width: 112px;
    margin: 0 10px;
    text-align: center;
    font-size: 14px;
}

.footer ul::after {
    content: "";
    display: block;
    clear: both;
}

.footer p {
    text-align: center;
    font-size: 12px;
}
.footer_text{
    color: white;
    font-size: 15px;
}
</style>
