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
    slides = cms_models.Slide.objects.all()
    numbers = index_models.Numbers.objects.all()
    reviews_images = index_models.Reviews_Image.objects.all()
    reviews = contacts_models.Review.objects.filter(is_published=True)
    partners = cms_models.Partners.objects.all()
    return render(request,'pages/base/index.html',locals())
    

def about(request):
    settings = cms_models.Settings.objects.first()
    return render(request,'pages/base/about.html',locals())