require('./scss/rich_saler.scss')

Vue.component('com-rich-saler',{
    props:['saler'],
    template:`<div class="com-rich-saler">
        <img :src="saler.head" alt="">
        <div>
            <span v-text="saler.name"></span>
        </div>

    </div>`
})