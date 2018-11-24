from helpers.director.shortcut import TablePage, ModelTable, ModelFields, page_dc, director
from .models import YewuGroup

class YewuGroupPage(TablePage):
    template = 'jb_admin/table.html'
    def get_label(self): 
        return '业务分组'
    
    class tableCls(ModelTable):
        pop_edit_field = 'id'
        model = YewuGroup
        exclude = []

class YewuGroupForm(ModelFields):
    class Meta:
        model = YewuGroup
        exclude = []
        
        
director.update({
    'yewugroup': YewuGroupPage.tableCls,
    'yewugroup.edit': YewuGroupForm,
})
page_dc.update({
    'yewugroup': YewuGroupPage,
})