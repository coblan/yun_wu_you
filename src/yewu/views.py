from django.shortcuts import render
from django.views.generic.base import View
from helpers.director.engine import BaseEngine
from webpage.models import Banners
from .structure import get_home_menu
from webpage.models import MainMenu, Action, ActionGroup
from helpers.director.model_func.dictfy import to_dict
from .models import Yewu, Saler
from webpage.models import YewuRecomItem, YewuRecomPanel
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
            {'label':'首页','link':'/p/home','name':'home'},
            {'label':'工商注册','link':'/p/3d','name':'3d'},
            {'label':'VR展馆','link':'/p/vr','name':'vr'},
            {'label':'全景现场','link':'/p/fullscreen','name':'fullscreen'},            
        ]
    
    def get_page_menu(self):
        mainmenu_list = []
        for menu in MainMenu.objects.all():
            mainmenu_list.append(
                {'label': menu.label, 'name': menu.label, 'action_group_list': [
                    {'label': group.label, 'link': group.yewu.get_url() if group.yewu else '', 'action_list': [
                        {'label': act.label, 'link': act.yewu.get_url() if act.yewu else '', 'highlight': act.highlight,} for act in group.action_set.all()
                        ],} for group in menu.actiongroup_set.all()
                    ],}
            )
        
        return mainmenu_list
        
    def extraCtx(self):
        banners = [{'img': x.img, 'target_url': x.link} for x in Banners.objects.filter(belong = 1).order_by('-priority')]
        recomPanels = []
        for panel in YewuRecomPanel.objects.filter(belong = 1):
            dc = to_dict(panel)
            dc['yewus'] = [to_dict(inst) for inst in panel.yewurecomitem_set.all()]
            recomPanels.append(dc)        
        return {
            'banners': banners,
            'recomPanels': recomPanels,
            'crt_page_name':'home',
            'header_bar_menu':self.get_header_menu(),
            'page_menu':self.get_page_menu()
        }

    def get_template(self):
        return 'yewu/home.html'
    
class YewuPage(Home):
    def extraCtx(self):
        yewu_pk = self.request.GET.get('yewu')
        yewu_inst = Yewu.objects.get(pk = yewu_pk)
        yewu_dict = to_dict(yewu_inst)
        
        yewu_dict['soldtype'] = [to_dict(inst) for inst in yewu_inst.soldtype_set.all().order_by('-priority')]
        
        yewu_dict['area_options'] = [{'value': x.pk, 'label': str(x),} for x in yewu_inst.av_area.all()]
        
        salers = [to_dict(inst) for inst in Saler.objects.all()]
        

        
        return {
            'yewu': yewu_dict,
            'salers': salers,
            'crt_page_name':'home',
            'header_bar_menu':self.get_header_menu(),
            'page_menu':self.get_page_menu()
        }
    
    def get_template(self):
        return 'yewu/yewu.html'    