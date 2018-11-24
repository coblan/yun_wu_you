from helpers.director.shortcut import ModelTable, ModelFields, TablePage, page_dc, director
from .models import RichPage, FooterLink


class FooterLinkPage(TablePage):
    template = 'jb_admin/table_new.html'
    def get_label(self): 
        return 'Footer链接'
    
    class tableCls(ModelTable):
        pop_edit_field = 'id'
        model = FooterLink
        exclude = []
        
        def dict_head(self, head): 
            if head['name'] == 'links':
                head['editor'] = 'com-table-array-obj-shower'
            return head

class FooterForm(ModelFields):
    class Meta:
        model = FooterLink
        exclude = []
    
    def dict_head(self, head): 
        if head['name'] == 'links':
            head['editor'] = 'com-field-table-list'
            head['table_heads'] = [{'name':'label','label':'显示文字','editor':'com-table-pop-fields-local', 'width': 120,}, 
                                   {'name':'url','label':'url', 'width': 200,},
                                   {'name': 'op', 'label': '', 'editor': 'com-table-change-order',}]
            head['fields_heads'] = [{'name':'label','label':'显示文字','editor':'linetext', 'required': True,}, 
                                    {'name':'richpage','label':'单页面','editor':'com-field-select', 'options': [
                                        {'value': x.pk, 'label': x.title,} for x in RichPage.objects.all()
                                        ],},
                                    {'name':'url','label':'链接','editor':'linetext', 'help_text': '链接到其他地址。如果设置了这个链接，则优先使用该链接而不是单页面。',},
                                    ]   
        return head


director.update({
    'footerlink': FooterLinkPage.tableCls,
    'footerlink.edit': FooterForm,
})

page_dc.update({
    'footerlink': FooterLinkPage,
})