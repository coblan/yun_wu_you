from .views import Home
from webpage.models import RichPage
from django.shortcuts import render

class RichPagePort(Home):
    def get(self, request, name): 
        rich = RichPage.objects.get(name = name)
        ctx = self.base_context()
        ctx.update({
            'rich_content': rich.content,
            'extend_menu': False,
        })
        return render(request, 'yewu/richpage.html', context = ctx)