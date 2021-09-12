from django.shortcuts import render
from django.http import HttpResponse

def returnLandingPage(request):
    return render(request, 'landingPageV1.html')
