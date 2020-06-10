# Django
from django.db import models

# Utilities
from footballon.utils.models import FootballonModel

class SportField(FootballonModel):
  """ Sport field model.

  Sport fields are offered through the platform to organize matches.
  """

  owner = models.ForeignKey('users.User', on_delete=models.CASCADE)
  owner_profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

  name = models.CharField('field name', max_length=140)
  address = models.CharField('field address', max_length=255)

  latitude = models.FloatField(null=True)
  longitude = models.FloatField(null=True)

  is_available_today = models.BooleanField(default=False)

