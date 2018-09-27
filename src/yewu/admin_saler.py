from helpers.director.shortcut import ModelTable, TablePage, ModelFields, page_dc, director
from .models import Saler

class SalerTablePage(TablePage):
    template = 'jb_admin/table.html'

    def get_label(self): 
        return '业务员管理'
    
    class tableCls(ModelTable):
        model = Saler
        exclude = []
        pop_edit_field = 'name'
        
        def dict_head(self, head): 
            width_dc = {
                'name': 120,
                'head': 200,
                'phone': 200,
            }
            if head['name'] in width_dc:
                head['width'] = width_dc.get(head['name'])

            return head

class SalerForm(ModelFields):
    class Meta:
        model = Saler
        exclude = []
    
    def dict_head(self, head): 
        if head['name'] == 'slogan':
            head['editor'] = 'blocktext'
        return head

director.update({
    'saler': SalerTablePage.tableCls,
    'saler.edit': SalerForm,
})

page_dc.update({
    'saler': SalerTablePage,
})