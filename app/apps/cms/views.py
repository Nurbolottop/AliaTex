from typing import dataclass_transform
from django.shortcuts import render
from apps.cms import models as cms_models
from apps.index import models as index_models
from apps.contacts import models as contacts_models
# Create your views here.
def index(request):
    settings = cms_models.Settings.objects.first()
    about_index = index_models.About.objects.first()
    services = cms_models.Service.objects.all()
    numbers = index_models.Numbers.objects.all()
    reviews = contacts_models.Review.objects.filter(is_published=True)
    partners = cms_models.Partners.objects.all()
    items = cms_models.OurService.objects.all()

    return render(request,'pages/base/index.html',locals())
    
def reviews(request):
    settings = cms_models.Settings.objects.first()
    return render(request,'pages/forms/reviews.html',locals())

# def gallery(request): 
#     settings = cms_models.Settings.objects.first()
#     return render(request,'pages/secondary/gallery.html',locals())
