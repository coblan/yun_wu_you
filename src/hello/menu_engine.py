# encoding:utf-8

from __future__ import unicode_literals
from helpers.director.shortcut import page_dc
from helpers.director.engine import BaseEngine,page,fa,can_list,can_touch
from django.contrib.auth.models import User,Group
from helpers.func.collection.container import evalue_container
from helpers.maintenance.update_static_timestamp import js_stamp
from django.utils.translation import ugettext as _
from django.conf import settings



class PcMenu(BaseEngine):
    url_name='admin'
    #brand = 'SportsCenter'
    #mini_brand='SC'
    brand = '管理后台'
    mini_brand='管理' 
    

    @property
    def menu(self):
        crt_user = self.request.user
        menu=[
            #{'label':_('DashBoard'),'url':page('home'),'icon':fa('fa-home'), 'visible':True}, 

            
            #{'label':_('业务管理'),'url':page('Business'),'icon':fa('fa-home'), 'visible':True, }, 
            
            {'label':'业务管理','icon':fa('fa-user'),'visible':True,
                 'submenu':[
                    {'label':'区域','url':page('Area'),'visible':can_touch(User, crt_user)},
                    {'label':'业务分组','url':page('yewugroup'),'visible':can_touch(User, crt_user)},
                    {'label': '业务', 'url': page('Business'),'icon':fa('fa-home'), 'visible':True,}, 
                    {'label':'业务员管理','url':page('saler'),'visible':can_touch(User, crt_user)},
                    {'label': '业务推广', 'url': page('YewuRecomPanel'), 'visible': True,}
                           ]},  
            #{'label':_('区域管理'),'url':page('Area'),'icon':fa('fa-home'), 'visible':True}, 
            {'label':'菜单管理','icon':fa('fa-user'),'visible':True,
                 'submenu':[
                    {'label': '第一层菜单', 'url': page('mainmenu'), 'visible': True,}, 
                    {'label': '第二层菜单', 'url': page('actiongroup'),'visible': True,}, 
                     {'label': '第三层菜单', 'url': page('action'),'visible': True,}, 
                   ]},  
            
            {'label':'其他页面管理','icon':fa('fa-user'),'visible':True,
                 'submenu':[
                     {'label':'滚动图片','url':page('banner'),'visible':can_touch(User, crt_user)},
                     {'label': 'richpage', 'url': page('richpage'),}, 
                     {'label': 'Footer', 'url': page('footerlink'), }, 
                     {'label': '沟通方式', 'url': page('qq_cfg'),}, 
                     {'label': '备案信息', 'url': page('beian_cfg'),}
                   ]},  

            {'label':_('User'),'icon':fa('fa-user'),'visible':True,
                 'submenu':[
                     {'label':_('User'),'url':page('jb_user'),'visible':can_touch(User, crt_user)},
                     {'label':_('权限组'),'url':page('jb_group'),'visible':can_touch(Group, crt_user)},
                     #{'label':'权限分组','url':page('group_human'),'visible':can_touch(Group)},
                   ]},   
            ]
        return menu

PcMenu.add_pages(page_dc)