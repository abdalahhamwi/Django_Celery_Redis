from django.urls import path
from . import views

urlpatterns = [
    path('',views.send_campaign_emails, name='send_campaign_emails' ),
]
