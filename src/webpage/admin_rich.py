from helpers.director.shortcut import ModelTable, ModelFields, TablePage, page_dc, director
from .models import RichPage

class RichPageTablePg(TablePage):
    template = 'jb_admin/table.html'
    def get_label(self): 
        return '单页面编辑'
    
    class tableCls(ModelTable):
        model = RichPage
        exclude = []
        
        def get_operation(self): 
            ops = super().get_operation()
            for op in ops:
                if op['name'] == 'add_new':
                    op['tab_name'] = 'edit_form'
                    op['ctx_name'] = 'richpageTabs'
            return ops
        
        def dict_head(self, head): 
            if head['name'] == 'id':
                head['editor'] = 'com-table-switch-to-tab'
                head['tab_name']='edit_form'
                head['ctx_name'] = 'richpageTabs'
            return head
        

    def get_context(self): 
        ctx = super().get_context()
        form_obj = RichForm(crt_user= self.crt_user)
        ls = [
          {'name':'edit_form',
           'label':'基本信息',
           'com':'com-tab-fields',
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
          ]
        ctx['named_ctx'] = {
            'richpageTabs': ls
            }
        return ctx
    
class RichForm(ModelFields):
    class Meta:
        model = RichPage
        exclude = []
    
    def dict_head(self, head): 
        if head['name'] == 'content':
            head['editor'] = 'richtext'
        return head

director.update({
    'richpage': RichPageTablePg.tableCls,
    'richpage.edit': RichForm,
})

page_dc.update({
    'richpage': RichPageTablePg,
})