from helpers.director.shortcut import ModelTable, ModelFields, TablePage, page_dc, director
from .models import YewuRecomPanel, YewuRecomItem

class YewuRecomPanelPage(TablePage):
    template = 'jb_admin/table.html'
    def get_label(self): 
        return '业务推广'
    
    class tableCls(ModelTable):
        model = YewuRecomPanel
        exclude = []
        hide_fields = ['id']
        
        def dict_head(self, head): 
            width_dc = {
                'title': 180,
                'sub_title': 200,
            }
            if head['name'] in width_dc:
                head['width'] = width_dc.get(head['name'])
                
            if head['name'] == 'title':
                head['editor'] = 'com-table-switch-to-tab'
                head['tab_name']='base_form'
            return head
        
        def get_context(self): 
            ctx = super().get_context()
            form_obj = YewuRecomForm(crt_user= self.crt_user)
            ls = [
                {'name':'base_form',
                 'label':'基本信息',
                 'com':'com_tab_fields',
                 'get_data':{
                     'fun':'get_row',
                     'kws':{
                        'director_name':form_obj.get_director_name(),
                        'relat_field':'pk',              
                     }
                 },
                 'after_save':{
                     'fun':'update_or_insert'
                     #'fun':'do_nothing'
                     #'fun':'update_par_row_from_db'
                 },
                 'heads': form_obj.get_heads(),
                 'ops': form_obj.get_operations()                 
                 }, 
                
                {
                    'name': 'soldtype',
                    'label': '推介业务',
                    'com': 'com_tab_table',
                    'par_field': 'pk',
                    'tab_field': 'recom_panel',
                    'table_ctx': YewuRecomItemTable(crt_user= self.crt_user).get_head_context(),
                    'visible': True,
                }

            ]
            ctx['tabs'] = ls
            return ctx

class YewuRecomForm(ModelFields):
    class Meta:
        model = YewuRecomPanel
        exclude = []
    
class YewuRecomItemTable(ModelTable):
    model = YewuRecomItem
    exclude = []
    hide_fields = ['recom_panel', 'id']
    pop_edit_field = 'title'
    def inn_filter(self, query): 
        query = super().inn_filter(query)
        if self.kw.get('recom_panel'):
            return query.filter(recom_panel=self.kw.get('recom_panel'))
        else:
            return query 
    
    def dict_head(self, head): 
        dc = {
            'yewu': 200,
            'title': 200,
            'sub_title': 200,
            'cover': 150,
        }
        if dc.get(head['name']):
            head['width'] = dc.get(head['name'])
        if head['name'] == 'yewu':
            head['editor'] = 'com-table-append-html-shower'
        return head
    
    def dict_row(self, inst): 
        return {
            '_html_yewu' : r'<a href="/yewu?yewu=%(pk)s" target="_blank">%(yewu)s</a>' % {'pk': inst.pk, 'yewu': str(inst.yewu),},
        }

class YewuRecomItemForm(ModelFields):
    hide_fields = ['recom_panel']
    def __init__(self, dc={}, pk=None, crt_user=None, nolimit=False, *args, **kw): 
        super().__init__(dc, pk, crt_user, nolimit, *args, **kw)
        if self.kw.get('recom_panel'):
            self.instance.recom_panel = YewuRecomPanel.objects.get(pk = self.kw.get('recom_panel'))
            
    class Meta:
        model = YewuRecomItem
        exclude = []
        

director.update({
     'YewuRecomPanel': YewuRecomPanelPage.tableCls,
     'YewuRecomPanel.edit': YewuRecomForm,
     
     'YewuRecomItemTable': YewuRecomItemTable,
     'YewuRecomItemTable.edit': YewuRecomItemForm,
})

page_dc.update({
    'YewuRecomPanel': YewuRecomPanelPage,
})