from django.shortcuts import render, redirect
from django.db.models import Avg, Max, Min, Sum
from django.contrib import messages
import random


# from django.template import loader
# from django.http import Http404
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import get_object_or_404
# from django.urls import reverse

from .models import nfl_team, nfl_scores
#  choice

# Create your views here.
def indexPageView(request) :
    teamVotes = nfl_team.objects.all().aggregate(Max('votes'))
    teamVotes = teamVotes['votes__max']
    teamName = nfl_team.objects.filter(votes=teamVotes)
    teamName = teamName[0]

    context = {
        "teamVotes" : teamVotes,
        "teamName" : teamName
    }
    return render(request, 'superbowlodds/index.html', context)

def gamesPageView(request) :
    Team = nfl_scores.objects.all()

    # years = []
    # for year in range(1966, 2023):
    #     years.append(year)

    # teamName = nfl_team.objects.filter(votes=teamVotes)


    context = {
        "teams": Team,
    }

    return render(request, 'superbowlodds/games.html', context)

# def simulationDisplayPageView(request) :
#     if request.method == 'POST':
#         form = SimulationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             team1 = form.cleaned_data['team1']
#             team2 = form.cleaned_data['team2']

#             return redirect('simulationDisplay')
#     else:
#         form = SimulationForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'superbowlodds/simulationSelect.html', context)

def simulationSelectPageView(request) :
    teams = nfl_team.objects.all()
    
    if request.method == 'POST':
        gameSim = nfl_scores()
        if (request.POST['team1'] == '') or (request.POST['team2'] == ''): 
            messages.success(request, ("Enter a valid team value."))

        gameSim.team_home = request.POST['team1']
        gameSim.team_away = request.POST['team2']

        # score_list = [0, 7, 10, 14, 17, 21, 24, 28, 32, 35, 38, 42, 49]
        score_list = [49]
        home_score = random.choice(score_list)
        away_score = random.choice(score_list)

        if home_score > away_score:
            result = gameSim.team_home + 'WIN!'
        elif home_score < away_score:
            result = gameSim.team_away + 'WIN!'
        else :
            result = "it's a TIE!"


        gameSim.score_home = home_score
        gameSim.score_away = away_score

        result_message = ['FINAL SCORE: ', str(home_score) + ' - ' + str(away_score), result]

        gameSim.save()

        context = {
        "teams" : teams,
        'result_message': result_message
        }
        return render(request, 'superbowlodds/simulationSelect.html', context)

    context = {
        "teams" : teams,
    }
    return render(request, 'superbowlodds/simulationSelect.html', context)

def simulationDisplayPageView(request, team_id1, team_id2
    ) :
    # team1 = nfl_team.objects.all(team_id = team_id1)
    team1 = nfl_team.objects.all(team_id = team_id1)
    team2 = nfl_team.objects.all(team_id = team_id2)

    gameSim = nfl_scores()
    gameSim.team_home = request.POST['team1']
    gameSim.team_away = request.POST['team2']

    context = {
        "team1" : team1,
        "team2" : team2,
        "gameSim": gameSim
    }
    return render(request, 'superbowlodds/simulationDisplay.html', context)

def teamsPageView(request) :
    # data = nfl_scores.objects.get(team_id = team_id)
    teams = nfl_team.objects.all()
    teams = sorted(teams, key=lambda ur: (-ur.votes))
    games = nfl_scores.objects.all()
    
    context = {
        "teams" : teams,
        "games" : games
    }
    return render(request, 'superbowlodds/voting.html', context)

def votingPageView(request, team_id) :
    data = nfl_team.objects.get(team_id = team_id)
    data.votes = (data.votes + 1)
    data.save()

    return redirect('teams')

def historyPageView(request) :
    return render(request, 'superbowlodds/history.html')
