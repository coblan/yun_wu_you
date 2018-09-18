from django.db import models
from helpers.director.model_func.cus_fields.cus_picture import PictureField
# Create your models here.
from yewu.models import Yewu
NAME_PAGES = (
    (1, '主页'), 
    (2, '工商')
)

class Banners(models.Model):
    img = PictureField('图片', max_length = 200, blank = False)
    link = models.CharField('链接', max_length = 500)
    belong = models.IntegerField('显示页面', choices= NAME_PAGES, default= 1)
    priority = models.IntegerField('优先级', default= 0, help_text= '越大，优先级越高')
    
class MainMenu(models.Model):
    label = models.CharField('显示名', max_length = 30)
    is_show = models.BooleanField('显示', default = True)
    priority = models.IntegerField('优先级', default = 0)
    
    def __str__(self): 
        return self.label    

class ActionGroup(models.Model):
    label = models.CharField('显示名', max_length = 100)
    yewu = models.ForeignKey(Yewu, verbose_name = '访问业务', blank = True, null = True)
    menu = models.ForeignKey(MainMenu, verbose_name = '父级菜单', blank = True, null = True)
    priority = models.IntegerField('优先级', default = 0)
    
    def __str__(self): 
        return self.label

class Action(models.Model):
    label = models.CharField('显示名', max_length = 100)
    yewu = models.ForeignKey(Yewu, verbose_name = '访问业务', blank = True)
    group = models.ForeignKey(ActionGroup, verbose_name = '链接组', blank = True, null = True)
    priority = models.IntegerField('优先级', default = 0)
    highlight = models.BooleanField('高亮', default = False)
    
    def __str__(self): 
        return self.label   
    
class YewuRecomPanel(models.Model):
    title = models.CharField('大标题', max_length = 200)
    sub_title = models.CharField('小标题', max_length = 300)
    belong = models.IntegerField('显示页面', choices= NAME_PAGES, default= 1)
    priority = models.IntegerField('优先级', default= 0, help_text= '越大，优先级越高')
    
    def __str__(self): 
        return self.title

class YewuRecomItem(models.Model):
    yewu = models.ForeignKey(Yewu, verbose_name = '展示业务')
    recom_panel = models.ForeignKey(YewuRecomPanel, verbose_name = '从属于')
    title = models.CharField('大标题', max_length = 200)
    sub_title = models.CharField('小标题', max_length = 300)
    price = models.CharField('价格', max_length = 30)
    cover = PictureField('宣传图片', max_length = 200, blank = True)
    
    
    