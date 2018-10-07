"""yun_wu_you URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from hello.menu_engine import PcMenu
from django.conf.urls.static import static
from django.conf import settings
from helpers.authuser.engin_view import AuthEngine
from django.views.generic import RedirectView 
from yewu.views import Home, YewuPage, SalerListPage
from yewu.page_rich import RichPagePort
from yewu.page_search import SearchYewu
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/([\w\.]+)/?$',AuthEngine.as_view(),name=AuthEngine.url_name),
    
    url(r'^d/',include('helpers.director.urls'),name='director'),
    url(r'^pc/([\w\.]+)/?$',PcMenu.as_view(),name=PcMenu.url_name),
    url(r'^pc/?$',RedirectView.as_view(url='/pc/Business')),    
    url(r'^yewu/?$', YewuPage.as_view ()), 
    url(r'^saler/?$', SalerListPage.as_view()), 
    url(r'^yewu/search/?$', SearchYewu.as_view()), 
    url(r'^p/home/?$',Home.as_view(),), 
    url(r'^rich/([\w\.]+)/?$',RichPagePort.as_view(),), 
    url(r'^$',Home.as_view(),), 
    
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)