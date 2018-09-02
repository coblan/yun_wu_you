from django.shortcuts import render
from django.views.generic.base import View
from helpers.director.engine import BaseEngine
# Create your views here.
class Home(View):
    def get(self,request):
        self.request = request
        baseengine = BaseEngine()
        baseengine.request = request
        page_data ={}
        if request.user.is_authenticated():
            page_data['username']=request.user.username
        ctx={
            'page_data':page_data,
            'js_config':baseengine.getJsConfig()
        }
        ctx.update( self.extraCtx())
        template = self.get_template()
        return render(request,template,context=ctx)   
    
    def get_header_menu(self):
        return [
            {'label':'首页','link':'/p/zhanxun','name':'zhanxun'},
            {'label':'工商注册','link':'/p/3d','name':'3d'},
            {'label':'VR展馆','link':'/p/vr','name':'vr'},
            {'label':'全景现场','link':'/p/fullscreen','name':'fullscreen'},            
        ]
    
    def get_page_menu(self):
        return [
            {'label':'注册公司','name':'zhucegongshi'},
            {'label':'财税记账','name':'caisuijizhang'},
            {'label':'知识产权','name':'zhishichanquan'}            
        ]
    
    def extraCtx(self):
        return {
            'crt_page_name':'home',
            'header_bar_menu':self.get_header_menu(),
            'page_menu':self.get_page_menu()
        }
        #ls=[]
        #for zhan in ZhanXunModel.objects.all():
            #ls.append({'title':zhan.title,'pk':zhan.pk})
        #return {
            #'zhanxun':ls
        #}

    def get_template(self):
        return 'yewu/home.html'