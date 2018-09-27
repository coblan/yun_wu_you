from django.contrib import admin
from .models import Banners
from helpers.director.shortcut import TablePage, ModelTable, ModelFields, page_dc, director
from . import js_cfg
from . import admin_navigate
from . import admin_recom_panel
from . import admin_foot
from . import admin_rich

from . import admin_qq
from . import admin_beian
# Register your models here.
class BannerPage(TablePage):
    template = 'jb_admin/table.html'
    def get_label(self): 
        return '宣传图画'
    
    class tableCls(ModelTable):
        pop_edit_field = 'id'
        model = Banners
        exclude = []
        
        def dict_head(self, head): 
            if head['name'] == 'img':
                head['width'] = 500
            return head

class BannerForm(ModelFields):
    class Meta:
        model = Banners
        exclude = []

director.update({
    'banner': BannerPage.tableCls,
    'banner.edit': BannerForm,
})

page_dc.update({
    'banner': BannerPage,
})