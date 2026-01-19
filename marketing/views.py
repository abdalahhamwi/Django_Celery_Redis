from django.shortcuts import render
import time
from .tasks import send_email


# Create your views here.
def send_campaign_emails(request):
    
    # call celery task
    send_email.delay()

    return render(request, "campagin.html")
