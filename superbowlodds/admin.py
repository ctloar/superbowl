from django.contrib import admin
from .models import nfl_scores, nfl_team
# , choice
# Register your models here.

admin.site.register(nfl_team)
admin.site.register(nfl_scores)
# admin.site.register(choice)