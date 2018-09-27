require('./scss/rich_saler.scss')

Vue.component('com-rich-saler',{
    props:['saler'],
    template:`<div class="com-rich-saler">
        <img :src="saler.head" alt="">
        <div>
            <label v-text="saler.name"></label>

            <button class="btn btn-default btn-sm">免费电话咨询</button>
        </div>
        <hr>
        <div v-text="saler.slogan" style="text-align: left">
        </div>

    </div>`
})