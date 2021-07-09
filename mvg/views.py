# Create your views here.
#from django.contrib.auth.models import User
from django.contrib import messages
from django.db import models
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from .forms import CropManagementForm,GrowingCropCreateForm, VarietieCreateForm,AreaCreateForm,ManagementGroupCreateForm,VegetableCreateForm
from .models import Area,Coordinate,CropManagement,GrowingCrop, ManagementGroup,Varietie, Vegetable

class GrowingCropDelete(generic.DeleteView):
    model=GrowingCrop
    template_name="mvg/growingcrop_delete.html"

    success_url=reverse_lazy('mvg:growingcrop')

class GrowingCrop(generic.ListView):
    model = GrowingCrop

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user.pk).order_by('area','management_group')

class GrowingCropCreate(generic.CreateView):
    model=GrowingCrop
    form_class=GrowingCropCreateForm
    template_name="mvg/growingcrop_form.html"

    def get_form_kwargs(self):
         kwargs = super(GrowingCropCreate,self).get_form_kwargs()
         kwargs['area_pk']=self.kwargs['area_pk']
         kwargs['managementgroup_pk']=self.kwargs['managementgroup_pk']
         return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kwargs = super(GrowingCropCreate,self).get_form_kwargs()
        context['area']=get_object_or_404(Area, pk=self.kwargs['area_pk'])
        context['management_group']=get_object_or_404(ManagementGroup,pk=self.kwargs['managementgroup_pk'])
        
        return context

    def form_valid(self, form):
        growingcrop=form.save(commit=False)
        #growingcrop.area=get_object_or_404(Area,pk=self.kwargs['area_pk'])
        #growingcrop.management_group=get_object_or_404(ManagementGroup,pk=self.kwargs['managementgroup_pk'])

        x=form.cleaned_data.get('x')
        y=form.cleaned_data.get('y')
        w=form.cleaned_data.get('w')
        h=form.cleaned_data.get('h')
        growingcrop.coordinate=Coordinate.objects.create(x=x,y=y,w=w,h=h)
        growingcrop.user=self.request.user
        #messages.add_message(self.request, messages.SUCCESS, '登録しました！')
        self.object=growingcrop.save()
        return redirect('mvg:growingcrop')   

class AreaCerate(generic.CreateView):
    model=Area
    form_class=AreaCreateForm
    template_name="mvg/create_form.html"

    def form_valid(self, form):
        area=form.save(commit=False)
        x=form.cleaned_data.get('x')
        y=form.cleaned_data.get('y')
        w=form.cleaned_data.get('w')
        h=form.cleaned_data.get('h')
        area.coordinate=Coordinate.objects.create(x=x,y=y,w=w,h=h)

        self.object=form.save()
        return redirect('mvg:growingcrop')

class ManagementGroupCreate(generic.CreateView):
    model=ManagementGroup
    form_class=ManagementGroupCreateForm
    template_name="mvg/create_form.html"

    def form_valid(self, form):
        instance=form.save(commit=False)
        instance.user=self.request.user
        self.object=form.save()
        return redirect('mvg:growingcrop')

class VegetableCerate(generic.CreateView):
    model=Vegetable
    form_class=VegetableCreateForm
    template_name="mvg/create_form.html"

    def form_valid(self, form):
        instance=form.save(commit=False)
        instance.user=self.request.user
        self.object=form.save()
        return redirect('mvg:growingcrop')

class VarietieCerate(generic.CreateView):
    model=Varietie
    form_class=VarietieCreateForm
    template_name="mvg/create_form.html"

    def form_valid(self, form):
        instance=form.save(commit=False)
        instance.user=self.request.user
        self.object=form.save()
        return redirect('mvg:growingcrop')

class CropManagement(generic.FormView,generic.ListView):
    model = CropManagement
    form_class= CropManagementForm
    template_name="mvg/cropmanagement.html"

    def get_queryset(self):
        #management_obj=get_object_or_404(CropManagement, management_group=self.kwargs['mg_pk'])
        return super().get_queryset().filter(user=self.request.user.pk,management_group=self.kwargs['mg_pk'])

    def form_valid(self, form):
        instance=form.save(commit=False)
        instance.management_group=get_object_or_404(ManagementGroup,pk=self.kwargs['mg_pk'])
        instance.user=self.request.user
        self.object=form.save()
        return redirect('mvg:cropmanagement', mg_pk=self.kwargs['mg_pk'])
