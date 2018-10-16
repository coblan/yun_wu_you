from django.shortcuts import render
from django.views.generic.base import View
from helpers.director.engine import BaseEngine
from webpage.models import Banners
from .structure import get_home_menu
from webpage.models import MainMenu, Action, ActionGroup, RichPage
from helpers.director.model_func.dictfy import to_dict
from .models import Yewu, Saler
from webpage.models import YewuRecomItem, YewuRecomPanel, FooterLink
import json
from helpers.director.kv import get_value

import random
# Create your views here.
class Home(View):
    def get(self,request):
        self.request = request
        page_data ={}
        if request.user.is_authenticated():
            page_data['username']=request.user.username
        ctx={
            'page_data':page_data,
            'extend_menu': True,
        }
        ctx.update( self.extraCtx())
        ctx.update(self.base_context())
        template = self.get_template()
        return render(request,template,context=ctx)   
    
    def base_context(self): 
        """
        页面的基本数据。
        """
        baseengine = BaseEngine()
        baseengine.request = self.request        
        ctx = {
            'js_config':baseengine.getJsConfig(), 
            'page_menu':self.get_page_menu()
        }
        ctx.update(self.get_header_menu())
        ctx.update(self.footer_data())
        ctx.update(self.get_kv_value())
        return ctx
    
    def get_kv_value(self): 
        ls = ['qq', 'wechat_gzh', 'wechat_slogan', 'service_phone', 'service_time', 'beian_info', 'copyright']
        dc = {}
        for k in ls:
            dc[k] = get_value(k)
        return {
            'qq': dc,
        }
    
    def footer_data(self): 
        """
        footer_menu = [
            {'label': '关于一站到底', 'submenu': [
                {'label': '了解我们', }, 
                {'label': '加入我们', }, 
                ],}
        ]
        """
        footer_menu = []
        for foot in FooterLink.objects.all():
            links = json.loads(foot.links)
            ls = []
            for item in links:
                if item.get('url'):
                    link = item.get('url')
                elif item.get('richpage'):
                    link = '/rich/%s' % RichPage.objects.get(pk = item.get('richpage')).name
                else:
                    link = ''
                ls.append({'link': link, 
                           'label': item.get('label'),})
            footer_menu.append( {'label': foot.label,'submenu': ls,} )
            
        return {'footer_menu': footer_menu}
        
    def get_header_menu(self):
        ls = [
            {'label':'首页','link':'/p/home','name':'home'},
            {'label':'工商注册','link':'/yewu?yewu=2','name':'gongshang'},
            {'label':'知识产权','link':'/yewu?yewu=33','name':'zhishi'},
            {'label':'法律服务','link':'/yewu?yewu=63','name':'lawservice'},   
            {'label':'人事社保','link':'/yewu?yewu=52','name':'human'},  
             {'label':'一站财税','link':'/yewu?yewu=52','name':'calshui'},   
        ]
        return {'header_bar_menu':ls}
    
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
        
        
        random_salers = random.sample(salers, min(len(salers), 3))
        random_saler = random.choice(salers)
        return {
            'yewu': yewu_dict,
            'salers': random_salers,
            'recom_saler': random_saler,
            'crt_page_name':'home',
            'header_bar_menu':self.get_header_menu(),
            'page_menu':self.get_page_menu(), 
            'extend_menu': False,
        }
    
    def get_template(self):
        return 'yewu/yewu.html'    
    
class SalerListPage(Home):
    def extraCtx(self): 
        salers = [to_dict(x) for x in Saler.objects.all()]
        ctx = {
            'extend_menu': False,
            'salers': salers,
        }
        return ctx
    
    def get_template(self): 
        return 'yewu/saler_list.html'
