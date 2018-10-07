require('./scss/place_select.scss')
import {citys} from  './place_select_data.js'


Vue.component('com-big-city-select',{
    props:['value'],
    data:function(){
        return {
            citys:citys,
            contain_show:false,
        }
    },
    template:`<div style="height: 15px;display: inline-block">
    <div class="place-input" @mouseenter="contain_show=true" @mouseleave="contain_show=false">
        <div class="input">
            <span><i class="fa fa-map-marker"></i></span>
            <span v-text="value"></span>
            <span>[切换城市]</span>
        </div>

        <ul v-show="contain_show" class="item-contain">
            <li class="item" @click="set_value(city)" v-for="city in citys" v-text="city"></li>
        </ul>
    </div>
    </div>`,
    methods:{
        set_value:function(city){
            this.$emit('input',city)
            this.contain_show=false
            localStorage.setItem(`crt_city`, city);
            location.reload()
        },

    }

})