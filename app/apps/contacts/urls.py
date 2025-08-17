from django.urls import path
from apps.contacts import views as contacts_views

urlpatterns = [
    path('contact-request/', contacts_views.contact_request, name='contact_request'),
    path('review-submit/', contacts_views.review_submit, name='review_submit'),
]
