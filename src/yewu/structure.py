from helpers.director.shortcut import request_cache

structure = [
    {'name':'gongshizhuche','label':'公司注册','yewu':[
            {'name':'yewu_gongshizhuche','label':'公司注册'},
            {'name':'yewu_zhuchedizhi','label':'注册地址'},
            {'name':'yewu_dizhixufei','label':'地址续费'},
            {'name':'yewu_yinghangkaihu','label':'银行开户'},
        ]},
     {"name":'company_change','label':'公司变更','yewu':[
            {'name':'yewu_company_change_name',"label":'公司名称变更'},
            {'name':'faren_zhiben_change','label':'法人,高管或注册资本变更'}
        ]}
     
]

@request_cache
def get_options():
    ls =[]
    for domain in structure:
        for item in domain['yewu']:
            ls.append({'value':item['name'],'label':'%s/%s'%(domain['label'],item['label'])})
    return ls