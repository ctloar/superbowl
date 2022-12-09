from django.contrib import admin
from .models import nfl_scores, nfl_team
# Register your models here.

admin.site.register(nfl_team)
admin.site.register(nfl_scores)