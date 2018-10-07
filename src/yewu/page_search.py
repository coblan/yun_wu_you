from .views import Home
from helpers.director.shortcut import ModelTable
from .models import Yewu
from django.db.models import Q
from helpers.director.model_func.dictfy import sim_dict

class SearchYewu(Home):
    def extraCtx(self): 
        wd = self.request.GET.get('kwd')
        exp = Q(title__icontains = wd)
        exp = exp | Q(sub_title__icontains = wd)
        yewus = [sim_dict(x) for x in Yewu.objects.filter(exp)]
        return {
            'yewus': yewus,
            'extend_menu': False,
        }
    
    def get_template(self): 
        return 'yewu/search.html'

