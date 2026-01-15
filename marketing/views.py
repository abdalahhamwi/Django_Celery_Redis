from django.shortcuts import render
import time
# Create your views here.
def send_campaign_emails(request):
    
    for x in range(10):
        time.sleep(1)
        print(x)
    
    return render (request,'campagin.html')