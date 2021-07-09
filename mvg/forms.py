from django.utils import timezone
from django import forms
from django.db.models import fields
from .models import Area,GrowingCrop,Varietie,ManagementGroup,Vegetable,CropManagement

class GrowingCropCreateForm(forms.ModelForm):

    x=forms.IntegerField(label='x')
    y=forms.IntegerField(label='y')
    w=forms.IntegerField(label='w')
    h=forms.IntegerField(label='h')
    
    class Meta:
        model = GrowingCrop
        exclude = ('user', 'harvest_date_start', 'harvest_date_end','coordinate')

    def __init__(self, *args, **kwargs):
        self.area=kwargs.pop('area_pk',None)
        self.management_group=kwargs.pop('managementgroup_pk',None)

        super(GrowingCropCreateForm, self).__init__(*args, **kwargs)
        self.fields['area'].initial = self.area
        self.fields['management_group'].initial = self.management_group

class AreaCreateForm(forms.ModelForm):

    x=forms.IntegerField(label='x')
    y=forms.IntegerField(label='y')
    w=forms.IntegerField(label='w')
    h=forms.IntegerField(label='h')

    class Meta:
        model=Area
        exclude = ('user', 'coordinate')

    
class ManagementGroupCreateForm(forms.ModelForm):

    class Meta:
        model=ManagementGroup
        exclude = ('user',)

class VegetableCreateForm(forms.ModelForm):

    class Meta:
        model=Vegetable
        exclude = ('user',)

class VarietieCreateForm(forms.ModelForm):

    class Meta:
        model=Varietie
        exclude = ('user',)

class CropManagementForm(forms.ModelForm):

    class Meta:
        model=CropManagement
        exclude=('user','management_group')

    def __init__(self, *args, **kwargs):

        super(CropManagementForm, self).__init__(*args, **kwargs)
        self.fields['date'].initial = timezone.now().date()