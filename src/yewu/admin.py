from django.contrib import admin
from .models import Yewu,Saler,Area, SoldType
from helpers.director.shortcut import ModelTable,ModelFields,TablePage,page_dc,director, RowFilter, RowSort
from .structure import get_options
from . import admin_yewu
from . import admin_saler
from . import admin_freephone
# Register your models here.

class BusinessPage(TablePage):
    template='jb_admin/table.html'
    def get_label(self):
        return '业务介绍'
    
    class tableCls(ModelTable):
        model = Yewu
        exclude=[]
        hide_fields = ['desp']
        
        def get_operation(self): 
            ops = super().get_operation()
            for op in ops:
                if op['name'] == 'add_new':
                    op['tab_name'] = 'bus_form'
            return ops    
        
        def dict_head(self, head):
            dc = {
                'title': 200,
                'sub_title': 200,
                'cover': 180,
            }
            if dc.get(head['name']):
                head['width'] = dc.get(head['name'])
            
            if head['name'] == 'title':
                head['editor'] = 'com-table-switch-to-tab'
                head['tab_name']='bus_form'
            #if head['name'] =='name':
                #head['editor'] ='com-table-label-shower'
            
            if head['name'] =='av_area':
                head['options'] = [{'value':x.pk,'label':str(x)} for x in Area.objects.all()]
            return head    
        
        def get_context(self): 
            ctx = super().get_context()
            ls = [
                {}
            ]
            ctx['tab'] = ls
            return ctx
        
        class filters(RowFilter):
            names = ['group']
    
    def get_context(self):
        ctx =super().get_context()
        form_obj = BusinessForm(crt_user=self.crt_user)
        ls = [
          {'name':'bus_form',
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
              'label': '销售套餐',
              'com': 'com_tab_table',
              'par_field': 'pk',
              'tab_field': 'yewu',
              'table_ctx': SoldTypeTable(crt_user= self.crt_user).get_head_context(),
              'show': 'pk != null',
              'visible': True,
          }
        ]
        ctx['tabs'] =ls
        return ctx
    
    

class BusinessForm(ModelFields):
    
    class Meta:
        model = Yewu
        exclude = []
    
    def dict_head(self, head):
        if head['name']=='desp':
            head['editor'] ='richtext'
        if head['name'] == 'name':
            head['editor']='com-field-select'
            head['options']=[]
            head['remote_options'] = 'business_options'
        return head
 
    @staticmethod
    def business_options(row = {}):
        options = get_options()
        already_bus =[x.name for x in  Yewu.objects.all() ]
        if row.get('pk'):
            already_bus.remove(row['name'])
        options= [x for x in options if x['value'] not in already_bus]
        return options

class SoldTypeTable(ModelTable):
    model = SoldType
    exclude = []
    hide_fields = ['yewu']
    pop_edit_field = 'label'
    
    @classmethod
    def clean_search_args(cls, search_args): 
        if not search_args.get('_sort'):
            search_args['_sort'] = '-priority'
        return search_args
    
    def inn_filter(self, query): 
        query = super().inn_filter(query)
        if self.kw.get('yewu'):
            return query.filter(yewu=self.kw.get('yewu'))
        else:
            return query
    def dict_head(self, head): 
        dc = {
            'priority': 120,
            'label': 250,
        }
        if dc.get(head['name']):
            head['width'] = dc.get(head['name'])
        return head
    
    class sort(RowSort):
        names = ['priority']

class SoldTypeForm(ModelFields):
    def __init__(self, dc={}, pk=None, crt_user=None, nolimit=False, *args, **kw): 
        super().__init__(dc, pk, crt_user, nolimit, *args, **kw)
        if self.kw.get('yewu'):
            self.instance.yewu = Yewu.objects.get(pk = self.kw.get('yewu'))
    hide_fields = ['yewu']
    class Meta:
        model = SoldType
        exclude = []


class AreaPage(TablePage):
    template='jb_admin/table.html'
    def get_label(self):
        return '区域管理'
    
    class tableCls(ModelTable):
        model = Area
        exclude =[]

class AreaForm(ModelFields):
    class Meta:
        model = Area
        exclude=[]
        

director.update({
    'Business':BusinessPage.tableCls,
    'Business.edit':BusinessForm,
    'Area':AreaPage.tableCls,
    'Area.edit':AreaForm,
    'business_options':BusinessForm.business_options,
    'yewu.soldtype-tab': SoldTypeTable,
    'yewu.soldtype-tab.edit': SoldTypeForm,
    
})

page_dc.update({
    'Business':BusinessPage,
    'Area':AreaPage,
})

