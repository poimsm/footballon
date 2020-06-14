from django.db import models
from footballon.utils.models import FootballonModel

class Player(FootballonModel):
  """Player model.

  A player is the table that holds the relationship between
  a user and a match.
  """

  BLACK = 0
  WHITE = 1
  TEAM_CHOICES = (
    (BLACK, 'Black'),
    (WHITE, 'White')
  )

  match = models.ForeignKey('matches.Match', on_delete=models.CASCADE)
  user = models.ForeignKey('users.User', on_delete=models.CASCADE)
  profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

  is_organizer = models.BooleanField(
    default=False,
    help_text='Set to true when the user has created the match.'
  )
  team = models.SmallIntegerField(
    choices=TEAM_CHOICES,
    default=BLACK,
    help_text='Players must choose a team when joining the match.'
  )

