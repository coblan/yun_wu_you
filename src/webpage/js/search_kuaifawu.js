
require('./scss/search_kuaifawu.scss')

Vue.component('com-search-kuaifawu',{
    props:['search_args','head'],
    template:`<div class="search-kuaifawu">
        <input type="text" :placeholder="head.placeholder"/>
        <span class="search-btn">搜索</span>
    </div>`
})