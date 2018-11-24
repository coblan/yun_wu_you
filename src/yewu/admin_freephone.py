from helpers.director.shortcut import TablePage, ModelFields, ModelTable, page_dc, director
from .models import FreePhone

class FreePhonePage(TablePage):
    class tableCls(ModelTable):
        model = FreePhone
        exclude = []

class FreePhoneForm(ModelFields):
    def __init__(self, dc={}, pk=None, crt_user=None, nolimit=False, *args, **kw): 
        return super().__init__(dc, pk, crt_user, nolimit= True, *args, **kw)
    class Meta:
        model = FreePhone
        exclude = []

director.update({
    'freephone': FreePhonePage.tableCls,
    'freephone.edit': FreePhoneForm,
})

page_dc.update({
    'freephone': FreePhonePage,
})