from django.db import models
from helpers.director.model_func.cus_fields.cus_picture import PictureField
# Create your models here.

class YewuGroup(models.Model):
    label = models.CharField('业务分组', max_length = 200)
    
    def __str__(self): 
        return self.label

class Yewu(models.Model):
    """
    """
    title = models.CharField('主标题',max_length=200)
    sub_title=models.CharField('副标题',max_length=600)
    cover = PictureField('封面', max_length = 200, blank = True)
    av_area=models.ManyToManyField('Area', verbose_name = '可用区域')
    desp = models.TextField('详细介绍',blank=True)
    group = models.ForeignKey(YewuGroup, verbose_name = '业务分组')
    
    def get_url(self): 
        return '/yewu?yewu=%s' % self.pk
    
    def __str__(self): 
        if getattr(self, 'group', None):
            return r'%(group)s/%(yewu)s' % {'group': self.group , 'yewu': self.title}
        else:
            return r'%(yewu)s' % { 'yewu': self.title}
    
class SoldType(models.Model):
    """
    """
    label=models.CharField('类型名称',max_length=100)
    org_price = models.FloatField('市场价',blank=True)
    price = models.FloatField('价格',blank=True)
    yewu= models.ForeignKey(Yewu,verbose_name='业务')
    priority = models.IntegerField(verbose_name= '优先级', default= 0)
    
class Area(models.Model):
    label = models.CharField('区域名',max_length =200)
    
    def __str__(self):
        return self.label
    

class Saler(models.Model):
    """销售人员"""
    name = models.CharField('人名',max_length=30)
    head= PictureField('头像',max_length=300)
    phone = models.CharField('手机号码',max_length=50)
    