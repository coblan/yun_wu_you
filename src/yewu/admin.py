from django.contrib import admin
from .models import Business,Saler,Area
from helpers.director.shortcut import ModelTable,ModelFields,TablePage,page_dc,director
from .structure import get_options

# Register your models here.

class BusinessPage(TablePage):
    template='jb_admin/table.html'
    def get_label(self):
        return '业务介绍'
    
    class tableCls(ModelTable):
        model = Business
        exclude=[]
    
        def get_operation(self): 
            ops = super().get_operation()
            for op in ops:
                if op['name'] == 'add_new':
                    op['tab_name'] = 'bus_form'
            return ops    
        
        def dict_head(self, head):
            if head['name'] == 'title':
                head['editor'] = 'com-table-switch-to-tab'
                head['tab_name']='bus_form'
            if head['name'] =='name':
                head['editor'] ='com-table-label-shower'
            
            if head['name'] =='av_area':
                head['options'] = [{'value':x.pk,'label':str(x)} for x in Area.objects.all()]
            return head    
        
        def dict_row(self, inst):
            options = get_options()
            for opt in options:
                if opt['value'] == inst.name:
                    label_name = opt['label']
                    break
                
            return {
                '_name_label':label_name
            }
    
    def get_context(self):
        ctx =super().get_context()
        form_obj = BusinessForm(crt_user=self.crt_user)
        ls = [
          {'name':'bus_form',
           'label':'业务介绍编辑',
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
        ]
        ctx['tabs'] =ls
        return ctx
    
    

class BusinessForm(ModelFields):
    class Meta:
        model = Business
        exclude = []
    
    def dict_head(self, head):
        if head['name']=='desp':
            head['editor'] ='richtext'
        if head['name'] == 'name':
            head['editor']='com-field-select'
            head['options']=[]
            head['remote_options'] = 'business_options'
        return head
    
    def dict_row(self, inst):
        options = get_options()
        label_name =''
        for opt in options:
            if opt['value'] == inst.name:
                label_name = opt['label']
                break
            
        return {
            '_name_label':label_name
        }    
    
    #def dict_row(self, inst):
        #options = get_options()
        #for opt in options:
            #if opt['value'] == inst.name:
                #label_name = opt['label']
                #break
            
        #return {
            #'_name_label':label_name
        #}    
    
    @staticmethod
    def business_options(row):
        options = get_options()
        already_bus =[x.name for x in  Business.objects.all() ]
        if row.get('pk'):
            already_bus.remove(row['name'])
        options= [x for x in options if x['value'] not in already_bus]
        return options


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
})

page_dc.update({
    'Business':BusinessPage,
    'Area':AreaPage,
})

