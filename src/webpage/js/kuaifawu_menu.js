require('./scss/kuaifawu_menu.scss')

Vue.component('com-kuaifawu-menu',{
    props:['label','menu_group'],
    data:function(){
        return {
            expand:false,
            active_menu:{}
        }
    }, //
    template:`<div class="kuaifawu-menu" @mouseenter="expand=true" @mouseleave="on_mouseleave()">

            <span  class="menu-button">
            <span class="action-icon"> <i class="fa fa-list-ul"></i></span>

               <span v-text="label"></span>
            </span>

            <div v-show="expand" class="actions">
                <com-kuaifawu-menu-item v-for="menu in menu_group" :menu="menu"
                    :class="['menu-item',{'active':active_menu.name==menu.name}]" @mouseenter.native="active_menu=menu"></com-kuaifawu-menu-item>
            </div>

            <!--业务菜单，展开部分-->
            <com-kuaifawu-menu-links class="menu-links" v-show="active_menu.name"
                :menu="active_menu"></com-kuaifawu-menu-links>
    </div>`,
    methods:{
        on_mouseleave:function(){
            this.expand=false
            this.active_menu={}
        }
    }

})

Vue.component('com-kuaifawu-menu-item',{
    props:['menu'],
    template:`<div>
        <span class="action-icon"><i class="fa fa-circle-o"></i></span>

        <span v-text="menu.label"></span>
    </div>`
})

Vue.component('com-kuaifawu-menu-links',{
    props:['menu'],
    template:`<div class="kuaifawu-menu-link">
        <table>
            <tr class="action_group" v-for="group in menu.action_group_list">
                <td class="group">
                    <label v-text="group.label"></label>
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