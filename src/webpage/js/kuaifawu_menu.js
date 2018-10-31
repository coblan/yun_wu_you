require('./scss/kuaifawu_menu.scss')

Vue.component('com-kuaifawu-menu',{
    props:['label','menu_group','extend_menu'],
    data:function(){
        return {
            org_expand:extend_menu,
            expand:false,
            active_menu:{}
        }
    }, //@mouseenter="expand=true" @mouseleave="on_mouseleave()"
    template:`<div class="kuaifawu-menu" @mouseenter="expand=true"  @mouseleave="on_mouseleave()">

            <span  class="menu-button">
               <span class="action-icon"> <i class="fa fa-list-ul"></i></span>
               <span v-text="label"></span>
            </span>

            <div v-show="expand || org_expand" class="actions">
                <com-kuaifawu-menu-item v-for="menu in menu_group" :menu="menu"
                    :class="['menu-item',{'active':active_menu.name==menu.name}]" @mouseenter.native="active_menu=menu"></com-kuaifawu-menu-item>
            </div>

            <!--业务菜单，展开部分-->
            <com-kuaifawu-menu-links class="menu-links" v-show="active_menu.name"
                :menu="active_menu" :style="my_style"></com-kuaifawu-menu-links>
    </div>`,
    computed:{
        my_style:function(){
            return {height: 55*this.menu_group.length +'px'}
        }
    },
    mounted:function(){
        //setTimeout(function(){
        //    $('.kuaifawu-menu-link').height( 60* this.menu_group.length )
        //})
    },
    methods:{
        on_mouseleave:function(){
            this.expand=false
            this.active_menu={}
        }
    }

})

Vue.component('com-kuaifawu-menu-item',{
    props:['menu'],
    template:`<div class="action com-kuaifawu-menu-item">
        <div class="center-v">
            <!--<span class="icon" v-if="menu.icon"><img :src="menu.icon" alt=""></span>-->
            <span class="icon" v-if="menu.icon" v-html="menu.icon"></span>
            <span v-else class="action-icon"><i class="fa fa-circle-o"></i></span>
            <span v-text="menu.label" style="display: inline-block;padding-left: 0.5rem"></span>
        </div>
    </div>`
})

Vue.component('com-kuaifawu-menu-links',{
    // 三级菜单  点击直接跳转页面
    props:['menu'],
    template:`<div class="kuaifawu-menu-link" >
        <table>
            <tr class="action_group" v-for="group in menu.action_group_list">
                <td class="group">
                    <label style="font-size: 110%"><a :href="group.link" v-text="group.label"></a></label>
                </td>
                <td class="link-panel">
                    <span class="link" v-for="act in group.action_list">
                        <a  :class="{highlight:act.highlight}" v-text="act.label" :href="act.link"></a>
                    </span>
                </td>
            </tr>
        </table>
    </div>`
})