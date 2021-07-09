# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.urls import path
from . import views

app_name = 'mvg'

urlpatterns = [
   path('', views.GrowingCrop.as_view(), name = 'growingcrop'),
   path('growingcrop_create/<int:area_pk>/<int:managementgroup_pk>/',views.GrowingCropCreate.as_view(), name='growingcrop_create'),
   path('growingcrop_delete/<int:pk>/',views.GrowingCropDelete.as_view(), name='growingcrop_delete'),
   path('cropmanagement/<int:mg_pk>/', views.CropManagement.as_view(), name = 'cropmanagement'),
   path('area_create/',views.AreaCerate.as_view(),name='area_create'),
   path('managementgroup_create/',views.ManagementGroupCreate.as_view(),name='managementgroup_create'),
   path('vegetable_create/',views.VegetableCerate.as_view(),name='vegetable_create'),
   path('vegetable_create/',views.VegetableCerate.as_view(),name='vegetable_create'),
   path('varietie_create/',views.VarietieCerate.as_view(),name='varietie_create'),
]
