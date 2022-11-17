from django.urls import path
from .views import indexPageView, standingsPageView, votingPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path('standings/', standingsPageView, name='standings'),  
    path('voting/', votingPageView, name='voting'),
]