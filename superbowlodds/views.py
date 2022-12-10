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
    teams = nfl_scores.objects.all()
    reset = False

    if request.method == 'POST':
        reset = True

        team_home = request.POST['team1']
        team_away = request.POST['team2']

        if request.POST['season'] == "All":
            teams = nfl_scores.objects.filter(team_home = team_home, team_away = team_away)
        else:
            schedule_season = request.POST['season']
            teams = nfl_scores.objects.filter(team_home = team_home, team_away = team_away, schedule_season = schedule_season)
        # teams = nfl_scores.objects.filter(team_home = team_home)

        team_info = nfl_team.objects.all()

        years = []
        start = 1966
        end = 2023
        
        # Check if start value is smaller than end value
        if start < end:
            # unpack the result
            years.extend(range(start, end))
            # Append the last value
            years.append(end)

        context = {
        "teams" : teams,
        "team_info" : team_info,
        "team_away" : team_away,
        "team_home" : team_home,
        "years" : years,
        "reset" : reset
        }
        return render(request, 'superbowlodds/games.html', context)

    team_info = nfl_team.objects.all()
    
    years = []
    start = 1966
    end = 2023
    
    # Check if start value is smaller than end value
    if start < end:
        # unpack the result
        years.extend(range(start, end))
        # Append the last value
        years.append(end)

    # for year in range(1966, 2023):
    #     years.append(year)

    # teamName = nfl_team.objects.filter(votes=teamVotes)


    context = {
        "teams" : teams,
        "team_info" : team_info,
        "years" : years,
        "reset" : reset
    }

    return render(request, 'superbowlodds/games.html', context)

def simulationSelectPageView(request) :
    teams = nfl_team.objects.all()
    
    if request.method == 'POST':
        gameSim = nfl_scores()
        if (request.POST['team1'] == '') or (request.POST['team2'] == ''): 
            messages.success(request, ("Enter a valid team value."))
        elif (request.POST['team1'] == request.POST['team2']): 
            messages.success(request, ("Enter a different away team."))
        else:
            home_team = request.POST['team1']
            away_team = request.POST['team2']

            gameSim.team_home = home_team
            gameSim.team_away = away_team

            score_list = [0, 7, 10, 14, 17, 21, 24, 28, 32, 35, 38, 42, 49]
            season = 2022


            # score_list = [49]
            home_score = random.choice(score_list)
            away_score = random.choice(score_list)
            week = "Offseason"
            season = 2022

            location = "Neutral"

            favoriteTeam = nfl_team.objects.get(team_name = home_team)
            favorite = favoriteTeam.team_id

            if home_score > away_score:
                result = gameSim.team_home + ' WIN!'
            elif home_score < away_score:
                result = gameSim.team_away + ' WIN!'
            else :
                result = "it's a TIE!"


            gameSim.score_home = home_score
            gameSim.score_away = away_score
            gameSim.schedule_week = week
            gameSim.schedule_season = season
            gameSim.team_favorite_id = favorite
            gameSim.stadium = location


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

# def simulationDisplayPageView(request, team_id1, team_id2
#     ) :
#     # team1 = nfl_team.objects.all(team_id = team_id1)
#     team1 = nfl_team.objects.all(team_id = team_id1)
#     team2 = nfl_team.objects.all(team_id = team_id2)

#     gameSim = nfl_scores()
#     gameSim.team_home = request.POST['team1']
#     gameSim.team_away = request.POST['team2']

#     context = {
#         "team1" : team1,
#         "team2" : team2,
#         "gameSim": gameSim
#     }
#     return render(request, 'superbowlodds/simulationDisplay.html', context)

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

def votingPageView(request, id) :
    data = nfl_team.objects.get(id = id)
    data.votes = (data.votes + 1)
    data.save()

    return redirect('teams')

def historyPageView(request) :
    return render(request, 'superbowlodds/history.html')

# Single profile page view
def showSingleGamePageView(request, game_id) :
    game = nfl_scores.objects.get(id = game_id)

    context = {
        "game" : game,
    }
    return render(request, 'superbowlodds/game_edit.html', context)

def updateGamesPageView(request):
    if request.method == 'POST':
        game_id = request.POST['game_id']
        game = nfl_scores.objects.get(id=game_id)

        game.team_home = request.POST['team_home']
        game.team_away = request.POST['team_away']
        game.score_home = request.POST['score_home']
        game.score_away = request.POST['score_away']
        game.stadium = request.POST['stadium']
        game.schedule_season = request.POST['schedule_season']
        game.schedule_week = request.POST['schedule_week']
        # if (game.schedule_playoff != True) | (game.schedule_playoff != False):
        #     game.schedule_playoff = None
        # else:
        #     game.schedule_playoff = request.POST['schedule_playoff']
        game.team_favorite_id = request.POST['team_favorite_id']                    

        game.save()
        return redirect('games')

    return gamesPageView(request)

def deleteGamePageView(request, game_id):
    '''
    It allows the user to delete food items from their food log
    '''
    # get the food log of the logged in user
    game = nfl_scores.objects.get(id=game_id)

    if request.method == 'POST':
        game.delete()
        return redirect('games')

    return render(request, 'superbowlodds/game_delete.html')
