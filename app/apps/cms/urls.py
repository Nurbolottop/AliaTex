from django.urls import path
from apps.cms import views as cms_views

urlpatterns = [
    path('', cms_views.index, name='index'),
    path('reviews', cms_views.reviews, name='reviews'),
    path('gallery', cms_views.gallery, name='gallery'),
]
