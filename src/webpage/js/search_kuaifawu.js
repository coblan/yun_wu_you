
require('./scss/search_kuaifawu.scss')

Vue.component('com-search-kuaifawu',{
    props:['search_args','head'],
    template:`<div class="search-kuaifawu">
        <input type="text" :placeholder="head.placeholder" v-model="search_args.kwd" @keyup.13="search()"/>
        <span class="search-btn" @click="search()">搜索</span>
    </div>`,
    methods:{
        search:function(){
            location=ex.appendSearch('/yewu/search',{kwd:this.search_args.kwd})
        }
    }
})