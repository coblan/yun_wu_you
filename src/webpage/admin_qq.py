from helpers.director.shortcut import FieldsPage, Fields, page_dc, director
from helpers.director.kv import get_value, set_value

class QQForm(FieldsPage):
    template = 'jb_admin/fields.html'
    def get_label(self): 
        return '沟通方式设置'
    
    class fieldsCls(Fields):
        def get_heads(self): 
            return [
                {'name': 'qq', 'label': 'QQ号码','editor': 'linetext',}, 
                {'name': 'wechat_gzh','label': '公众号二维码','editor': 'com-field-picture',}, 
                {'name': 'wechat_slogan','label': '公众号口号','editor': 'blocktext',}, 
                {'name': 'service_phone','label': '服务电话','editor': 'linetext',}, 
                {'name': 'service_time','label': '服务时间','editor': 'linetext',}
            ]
        
        def get_row(self): 
            return {
                'qq': get_value('qq'),
                'wechat_gzh': get_value('wechat_gzh'),
                'wechat_slogan': get_value('wechat_slogan'),
                'service_phone': get_value('service_phone'),
                'service_time': get_value('service_time'),
                '_director_name': 'qq_cfg',
            }
        
        def save_form(self): 
            ls = ['qq', 'wechat_gzh', 'wechat_slogan', 'service_phone', 'service_time', ]
            for k, v in self.kw.items():
                if k in ls and v:
                    set_value(k, v)


director.update({
    'qq_cfg': QQForm.fieldsCls,
})

page_dc.update({
    'qq_cfg': QQForm,
})