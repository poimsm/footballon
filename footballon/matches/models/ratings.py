# Django
from django.db import models

# Utilities
from footballon.utils.models import FootballonModel

class Rating(FootballonModel):
  """Rating model.

  Rates are entities that store the rating a player
  gave to a match, it ranges from 1 to 5.
  """

  user = models.ForeignKey('users.User', on_delete=models.SET_NULL)
  profile = models.ForeignKey('users.Profile', on_delete=models.SET_NULL)
  match = models.ForeignKey('matches.Match', on_delete=models.CASCADE)

  rating = models.SmallIntegerField(default=3)
  comment = models.CharField(max_length=255, null=True)


