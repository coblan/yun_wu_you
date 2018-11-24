
require('./scss/search_kuaifawu.scss')

Vue.component('com-search-kuaifawu',{
    props:['search_args','head'],
    template:`<div class="search-kuaifawu">
        <input type="text" :placeholder="head.placeholder" v-model="search_args.kwd" @keyup.13="search()"/>
        <span class="search-btn clickable" @click="search()">搜索</span>
    </div>`,
    methods:{
        search:function(){
            location=ex.appendSearch('/search',{kwd:this.search_args.kwd})
        }
    }
})