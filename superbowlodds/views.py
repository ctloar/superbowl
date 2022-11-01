from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return HttpResponse('LA Rams 2022 Champs! Boo Seahawks.')

def standingsPageView(request) :
    return HttpResponse('NFL Standings')

def votingPageView(request) :
    return HttpResponse('Voting Process')