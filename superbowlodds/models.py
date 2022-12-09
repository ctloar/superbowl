from django.db import models
from datetime import datetime, timedelta
# FORMS
# add team
# edit team
# add team game
# Create your models here.
class nfl_scores(models.Model):
    schedule_date = models.DateField(default=datetime.today, blank=True)
    schedule_season = models.IntegerField(max_length=4)
    schedule_week = models.CharField(max_length=30)
    schedule_playoff = models.BooleanField()
    team_home = models.CharField(max_length=75)
    score_home = models.IntegerField(max_length=20, blank=True)
    score_away = models.IntegerField(max_length=20, blank=True)
    team_away = models.CharField(max_length=75)
    team_favorite_id = models.CharField(max_length=4, blank=True)
    spread_favorite = models.DecimalField(max_digits=8, decimal_places=1, blank=True)
    over_under_line = models.DecimalField(max_digits=8, decimal_places=1, blank=True)
    stadium = models.CharField(max_length=50, blank=True)
    stadium_nuetral = models.BooleanField(blank=True)
    weather_temperature = models.IntegerField(blank=True)
    weather_wind_mph = models.IntegerField(blank=True)
    weather_humidity = models.IntegerField(blank=True)
    weather_detail = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return (self.result)
class nfl_team(models.Model):
    team_name = models.CharField(max_length=75)
    team_name_short = models.CharField(max_length=75)
    team_id = models.CharField(max_length=20)
    team_id_pfr = models.CharField(max_length=75)
    team_conference = models.CharField(max_length=75, blank=True)
    team_division = models.CharField(max_length=75, blank=True)
    team_conference_pre2002 = models.CharField(max_length=75, blank=True)
    team_division_pre2002 = models.CharField(max_length=75, blank=True)
    games = models.ManyToManyField(nfl_scores, blank=True)
    def __str__(self):
        return (self.team_id)