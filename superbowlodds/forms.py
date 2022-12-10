from django import forms
from .models import nfl_team, nfl_scores

class SimulationForm(forms.ModelForm):
    team1= forms.CharField(label='Select team 1', widget=forms.Select(choices=nfl_team.objects.all()))
    team2= forms.CharField(label='Select team 2', widget=forms.Select(choices=nfl_team.objects.all()))
    
    class Meta:
        model = nfl_scores
        fields = ("schedule_season", "schedule_week", "schedule_playoff", "team_home", "team_away")