from django.db import models
from footballon.utils.models import FootballonModel

class Hour(FootballonModel):
  date = models.DateTimeField()
  is_available =  models.BooleanField(default=True)
  sport_field = models.ForeignKey('fields.SportField', on_delete=models.CASCADE)
  taken_by = models.ForeignKey('users.user', on_delete=models.CASCADE)