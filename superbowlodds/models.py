from django.db import models
from datetime import datetime, timedelta

# FORMS
# add team
# edit team
# add team game

# Create your models here.
class game(models.Model):
    home_team_name = models.CharField(max_length=75)
    away_team_name = models.CharField(max_length=75)
    date = models.DateField(default=datetime.today, blank=True)
    result = models.BooleanField(default=True)
    opponent_team_score = models.IntegerField(max_length=20)
    home_team_score = models.IntegerField(max_length=20)

    def __str__(self):
        return (self.result) 

class team(models.Model):
    team_id = models.CharField(max_length=20)
    team_name = models.CharField(max_length=75)
    team_name_short = models.CharField(max_length=75)
    team_id_pfr = models.CharField(max_length=75)
    team_conference = models.CharField(max_length=75)
    team_conference_pre2002 = models.CharField(max_length=75)
    team_division_pre2002 = models.CharField(max_length=75)
    team_division = models.CharField(max_length=75)
    games = models.ManyToManyField(game, blank=True)

    def __str__(self):
        return (self.team_id) 