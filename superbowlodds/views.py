from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return render(request, 'superbowlodds/index.html')

def standingsPageView(request) :
    return render(request, 'superbowlodds/standings.html')

def votingPageView(request) :
    return render(request, 'superbowlodds/voting.html')