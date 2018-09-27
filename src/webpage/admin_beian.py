from helpers.director.shortcut import FieldsPage, Fields, page_dc, director
from helpers.director.kv import get_value, set_value

class BeianForm(FieldsPage):
    template = 'jb_admin/fields.html'
    def get_label(self): 
        return '备案信息'
    
    class fieldsCls(Fields):
        def get_heads(self): 
            return [
                {'name': 'beian_info', 'label': '备案信息','editor': 'linetext',}, 
                {'name': 'copyright','label': '版权声明','editor': 'linetext',}, 
            ]
        
        def get_row(self): 
            return {
                'beian_info': get_value('beian_info'),
                'copyright': get_value('copyright'),
                '_director_name': self.get_director_name(),
            }
        
        def save_form(self): 
            ls = ['beian_info', 'copyright', ]
            for k, v in self.kw.items():
                if k in ls and v:
                    set_value(k, v)


director.update({
    'beian_cfg': BeianForm.fieldsCls,
})

page_dc.update({
    'beian_cfg': BeianForm,
})