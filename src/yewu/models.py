from django.db import models

# Create your models here.

class Business(models.Model):
    """
    """
    name = models.CharField('标识名称',max_length=30)
    title = models.CharField('主标题',max_length=200)
    sub_title=models.CharField('副标题',max_length=600)
    av_area=models.ManyToManyField('Area',null=True)
    desp = models.TextField('详细介绍',blank=True)
    
    
class SoldType(models.Model):
    """
    """
    label=models.CharField('类型名称',max_length=100)
    org_price = models.FloatField('市场价',blank=True)
    price = models.FloatField('价格',blank=True)
    bus= models.ForeignKey(Business,verbose_name='业务')
    
class Area(models.Model):
    label = models.CharField('区域名',max_length =200)
    
    def __str__(self):
        return self.label
    

class Saler(models.Model):
    """销售人员"""
    name = models.CharField('人名',max_length=30)
    head=models.CharField('头像',max_length=300)
    phone = models.CharField('手机号码',max_length=50)
    