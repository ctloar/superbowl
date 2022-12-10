from django.urls import path
from .views import indexPageView, gamesPageView, teamsPageView, votingPageView
from .views import simulationSelectPageView, historyPageView
from .views import showSingleGamePageView, updateGamesPageView, deleteGamePageView

urlpatterns = [
    path('games/', gamesPageView, name='games'),
    path('history/', historyPageView, name='history'),  
    path('simulation/', simulationSelectPageView, name='simulationSelect'),
    path("showSingleGame/<int:game_id>/", showSingleGamePageView, name="single_game"),
    path("updateGames/", updateGamesPageView, name="update_game"),
    path('gameDelete/<int:game_id>/', deleteGamePageView, name='delete_game'),
    # path('simulation/<int:team_id1>/<int:team_id2>/', simulationDisplayPageView, name='simulationDisplay'),
    # path('simulation/<int:team_id1>/', simulationDisplayPageView, name='simulationDisplay'),
    path('teams/', teamsPageView, name='teams'),
    path('voting/<int:id>/', votingPageView, name='voting'),
    path("", indexPageView, name="index")
]