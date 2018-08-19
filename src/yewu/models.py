from django.db import models

# Create your models here.

class Yewu(models.Model):
    name = models.CharField('标识名称',max_length=30)
    title = models.CharField('主标题',max_length=200)
    sub_title=models.CharField('副标题',max_length=600)
    
    


class Yewuer(models.Model):
    name = models.CharField('人名',max_length=30)
    head=models.CharField('头像',max_length=300)
    phone = models.CharField('手机号码',max_length=50)
    