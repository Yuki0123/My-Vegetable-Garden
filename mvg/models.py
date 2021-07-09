from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Vegetable(models.Model):
    name = CharField('野菜',max_length=255)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)
    def __str__(self) -> str:
        return self.name

class Varietie(models.Model):
    vegetable = ForeignKey(Vegetable, verbose_name='野菜', on_delete=models.SET_NULL, null=True)
    name = CharField('品種', max_length=255)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Coordinate(models.Model):
    x = IntegerField('X座標')
    y = IntegerField('Y座標')
    w = IntegerField('幅')
    h= IntegerField('高さ')
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return '{},{},{},{}'.format(self.x,self.y,self.w,self.h)

class Field(models.Model):
    name = CharField('畑', max_length=255)
    coordinate = ForeignKey(Coordinate,verbose_name='座標', on_delete = models.CASCADE)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Area(models.Model):
    name = CharField('栽培エリア', max_length=255)
    field = ForeignKey(Field,verbose_name='畑', on_delete = models.CASCADE)
    coordinate = ForeignKey(Coordinate,verbose_name = '座標', on_delete = models.CASCADE)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class ManagementGroup(models.Model):
    name = CharField('管理グループ', max_length=255)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class CropManagement(models.Model):
    title = CharField('タイトル', max_length=255)
    text=TextField('内容', null=True, blank=True)
    date = DateField('実施日', null=True, blank=True)
    management_group = ForeignKey(ManagementGroup, verbose_name='管理グループ',  on_delete = models.CASCADE)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return self.title


class GrowingCrop(models.Model):
    variety = ForeignKey(Varietie,verbose_name='品種', null=True, on_delete = models.SET_NULL)
    area = ForeignKey(Area, verbose_name='栽培エリア', null=True, on_delete = models.SET_NULL)
    management_group = ForeignKey(ManagementGroup, verbose_name='管理グループ', null=True, on_delete = models.SET_NULL)
    seeding_date = DateField('種まき日', null=True, blank=True)
    planting_date = DateField('植付日', null=True, blank=True)
    transplanting_date = DateField('移植日', null=True, blank=True)
    harvest_date_start =  DateField('収穫開始日', null=True, blank=True)
    harvest_date_end =  DateField('収穫完了日', null=True, blank=True)
    coordinate = ForeignKey(Coordinate,verbose_name = '座標', null=True,on_delete = models.SET_NULL)
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self) -> str:
        return '{} {} {} {}'.format(self.area.field.name,self.area.name,self.variety.vegetable.name,self.variety.name)

