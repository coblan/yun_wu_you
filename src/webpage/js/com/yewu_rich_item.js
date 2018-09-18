require('./scss/yewu_rich_item.scss')

Vue.component('com-yewu-rich-item',{
    props:['yewu'],
    template:`<div class="com-yewu-rich-item clickable" @click="goto_yewu">
        <img :src="yewu.cover" alt="">
        <div class="info">
            <h4 class="title" v-text="yewu.title"></h4>
            <div class="sub-title" v-text="yewu.sub_title"></div>
            <div class="price" v-text="yewu.price"></div>
        </div>
    </div>`,
    methods:{
        goto_yewu:function(){
            location='/yewu?yewu='+this.yewu.pk
        }
    }
})