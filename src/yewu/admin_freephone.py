from helpers.director.shortcut import TablePage, ModelFields, ModelTable, page_dc, director
from .models import FreePhone

class FreePhonePage(TablePage):
    class tableCls(ModelTable):
        model = FreePhone
        exclude = []

class FreePhoneForm(ModelFields):
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