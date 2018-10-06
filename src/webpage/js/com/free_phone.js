require('./scss/free_phone.scss')

Vue.component('com-free-phone',{
    template:`<div class="free-phone">
    <el-steps :active="1" align-center>
          <el-step title="输入手机号" ></el-step>
          <el-step title="您接听来电" ></el-step>
          <el-step title="被叫方接听" ></el-step>
          <el-step title="咨询结束"></el-step>
    </el-steps>
        <div class="phone-row" >
             <input class="form-control" type="text" placeholder="手机号码">
              <button type="button" class="btn btn-success btn-sm">开始免费咨询</button>
        </div>
        <div style="text-align: center;width: 430px;margin: auto;margin-top: 3em;">
          <span>本次电话咨询完全免费，我们将对您的号码严格保密，请放心使用</span>
        </div>

    </div>`
})