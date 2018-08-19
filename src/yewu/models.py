from django.db import models

# Create your models here.

class Yewu(models.Model):
    name = models.CharField('标识名称',max_length=30)
    title = models.CharField('主标题',max_length=200)
    


class Yewuer(models.Model):
    pass