# Django
from django.db import models

# Utilities
from footballon.utils.models import FootballonModel

class Comment(FootballonModel):
  """Comment model.

  Players can leave comments in the public comment section of each match.
  """

  user = models.ForeignKey('users.User', on_delete=models.CASCADE)
  profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
  match = models.ForeignKey('matches.Match', on_delete=models.CASCADE)

  content = models.CharField(max_length=255, null=False)
