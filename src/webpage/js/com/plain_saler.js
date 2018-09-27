require('./scss/plain_saler.scss')

Vue.component('com-plain-saler',{
    props:['saler'],
    template:`<div class="com-plain-saler flex">
    <div class="inn-wrap">
        <img :src="saler.head" alt="">
        <div class="panel">
             <label v-text="saler.name"></label>
             <div class="info">
              <span>工作经验：</span><span v-text="saler.exp"></span>&nbsp;&nbsp; |&nbsp;&nbsp;
              <span>好评率：</span><span v-text="saler.comment"></span>
             </div>

             <div class="free-phone">
                <button class="btn btn-default btn-sm">免费电话咨询</button>
             </div>

        </div>
    </div>


    </div>`
})