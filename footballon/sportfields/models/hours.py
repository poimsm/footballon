from django.db import models
from footballon.utils.models import FootballonModel

class Hour(FootballonModel):
  """Hour model.

  Hours are issued by sports fields and can be reserved
  by users. After each reservation a new match will be created.
  """
  sport_field = models.ForeignKey('sportfields.SportField', on_delete=models.CASCADE)
  booked_by = models.ForeignKey('users.User', on_delete=models.SET_NULL)

  date = models.DateTimeField()
  is_available =  models.BooleanField(default=True)
