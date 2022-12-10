from django.urls import path
from .views import indexPageView, gamesPageView, teamsPageView, votingPageView
from .views import simulationSelectPageView, simulationDisplayPageView, historyPageView

urlpatterns = [
    path('games/', gamesPageView, name='games'),  
    path('history/', historyPageView, name='history'),  
    path('simulation/', simulationSelectPageView, name='simulationSelect'),
    # path('simulation/<int:team_id1>/<int:team_id2>/', simulationDisplayPageView, name='simulationDisplay'),
    # path('simulation/<int:team_id1>/', simulationDisplayPageView, name='simulationDisplay'),
    path('teams/', teamsPageView, name='teams'),
    path('voting/<int:team_id>/', votingPageView, name='voting'),
    path("", indexPageView, name="index")
]