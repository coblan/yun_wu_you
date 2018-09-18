from helpers.director.shortcut import ModelTable, TablePage, ModelFields, page_dc, director, RowFilter, RowSort
from .models import MainMenu, ActionGroup, Action

class MainMenuPage(TablePage):
    template = 'jb_admin/table.html'
    def get_label(self): 
        return '主菜单'
    
    class tableCls(ModelTable):
        pop_edit_field = 'id'
        model = MainMenu
        exclude = []
        
        @classmethod
        def clean_search_args(cls, search_args): 
            if not search_args.get('_sort'):
                search_args['_sort'] = '-priority'
            return search_args
        
        def dict_head(self, head): 
            dc = {
                'priority': 100,
            }
            if dc.get(head['name']):
                head['width'] = dc.get(head['name'])
            return head
        
        class sort(RowSort):
            names = ['priority']

class MainMenuForm(ModelFields):
    class Meta:
        model = MainMenu
        exclude = []


class ActionGroupPage(TablePage):
    template = 'jb_admin/table.html'
    def get_label(self): 
        return '链接分组'
    
    class tableCls(ModelTable):
        pop_edit_field = 'id'
        model = ActionGroup
        exclude = []
        @classmethod
        def clean_search_args(cls, search_args): 
            if not search_args.get('_sort'):
                search_args['_sort'] = '-priority'
            return search_args
        
        def dict_head(self, head): 
            dc = {
                'priority': 100,
                'link': 200,
            }
            if dc.get(head['name']):
                head['width'] = dc.get(head['name'])
            return head        
        class filters(RowFilter):
            names = ['menu']
            
        class sort(RowSort):
            names = ['priority']        
        

class ActionGroupForm(ModelFields):
    class Meta:
        model = ActionGroup
        exclude = []

class ActionPage(TablePage):
    template = 'jb_admin/table.html'
    def get_label(self): 
        return '业务链接'
    
    class tableCls(ModelTable):
        pop_edit_field = 'id'
        model = Action
        exclude = []
        
        @classmethod
        def clean_search_args(cls, search_args): 
            if not search_args.get('_sort'):
                search_args['_sort'] = '-priority'
            return search_args
        
        def dict_head(self, head): 
            dc = {
                'priority': 100,
                'link': 200,
            }
            if dc.get(head['name']):
                head['width'] = dc.get(head['name'])
            return head
        
        class filters(RowFilter):
            names = ['group']
            fields_sort = ['menu', 'group']
            def getExtraHead(self): 
                return [
                    {'name': 'menu', 'label': '主菜单','editor': 'com-select-filter','options': [
                        {'value': menu.pk, 'label': str(menu),} for menu in MainMenu.objects.all()
                        ],}, 
                    {'name': 'group',
                     'label': '链接分组',
                     'editor': 'com-related-select-filter',
                     'options': [],
                     'related': 'menu',
                     'director_name': 'groupoptions.dynamic'
                     }
                ]
            
            @staticmethod
            def getGroupOptions(related):
                menu_pk = related 
                query = ActionGroup.objects.filter(menu=menu_pk)
                options = [{'value': x.pk, 'label': str(x)} for x in query]
                return options            
            
            #def getExtraHead(self):
                #return [
                    #{
                        #'name': 'leaguename',
                        #'label': '联赛',
                        #'editor': 'com-related-select-filter',
                        #'options': [],
                        #'related': 'country',
                        #'director_name': 'league-filter', }
                #]            
        
        class sort(RowSort):
            names = ['priority']        

class ActionForm(ModelFields):
    class Meta:
        model = Action
        exclude = []

director.update({
    'mainmenu': MainMenuPage.tableCls,
    'mainmenu.edit': MainMenuForm,
    'actiongroup': ActionGroupPage.tableCls,
    'actiongroup.edit': ActionGroupForm,
    'action': ActionPage.tableCls,
    'action.edit': ActionForm,
    
    'groupoptions.dynamic': ActionPage.tableCls.filters.getGroupOptions,
    
})       

page_dc.update({
    'mainmenu': MainMenuPage,
    'actiongroup': ActionGroupPage,
    'action': ActionPage,
})