from django.urls import path
from apps.contacts import views as contacts_views

urlpatterns = [
    path('leave-review/', contacts_views.leave_review, name='leave_review'),
]
