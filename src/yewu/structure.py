from helpers.director.shortcut import request_cache
from helpers.func.dict_list import find_one
all_yewu = [
    {'name':'gongshizhuche','label':'公司注册','yewu_list':[
            {'name':'yewu_gongshizhuche','label':'公司注册'},
            {'name':'yewu_zhuchedizhi','label':'注册地址'},
            {'name':'yewu_dizhixufei','label':'地址续费'},
            {'name':'yewu_yinghangkaihu','label':'银行开户'},
        ]},
    {"name":'company_change','label':'公司变更','yewu_list':[
           {'name':'yewu_company_change_name',"label":'公司名称变更'},
           {'name':'faren_zhiben_change','label':'法人,高管或注册资本变更'}
       ]}, 
    {'name': 'tax_proxy', 'label': '财税记账', 'yewu_list': [
        {'name': 'small_enterprise_tax', "label": '小规模纳税人记账',}, 
        {'name': 'normal_enterprise_tax', 'label': '一般纳税人记账',}
        ],}
]

def get_home_menu(): 
    """
    {'label': '注册公司', 
    'yewu_group_names': ['gongshizhuche',  'company_change'],
    'yewu_groups':[
        item = all_yewu的项
    ]
    ''
    }, 
    """
    home_menu = [
        {'label': '注册公司', 'name': 'gongshizhuche', 'yewu_group_names': ['gongshizhuche',  'company_change']}, 
        {'label': '财税记账', 'name': 'calwu','yewu_group_names': ['tax_proxy'],}
    ]
    for menu in home_menu:
        ls = menu.get('yewu_group_names')
        menu['yewu_groups'] = []
        for group in ls:
            yewu_group = find_one(all_yewu, {'name': group,})
            menu['yewu_groups'].append(yewu_group)
    return home_menu
            




@request_cache
def get_options():
    ls =[]
    for domain in all_yewu:
        for item in domain['yewu_list']:
            ls.append({'value':item['name'],'label':'%s/%s'%(domain['label'],item['label'])})
    return ls