require('./scss/plain_saler.scss')

Vue.component('com-plain-saler',{
    props:['saler'],
    template:`<div class="com-plain-saler">
        <img :src="saler.head" alt="">
        <span v-text="saler.name"></span>
    </div>`
})