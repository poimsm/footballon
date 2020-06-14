# Django
from django.db import models

# Utilities
from footballon.utils.models import FootballonModel

class Profile(FootballonModel):
  """Profile model.

  A profile holds a user's public data like biography, picture,
  and statistics.
  """

  user = models.OneToOneField('users.user', on_delete=models.CASCADE)
  
  picture = models.ImageField(
    'profile picture',
    upload_to='users/pictures/',
    blank=True,
    null=True
  )

  # stats
  matches_played = models.PositiveIntegerField(default=0)
  matches_created = models.PositiveIntegerField(default=0)

  reputation = models.FloatField(
    default=3.5,
    help_text=(
      'The reputation of players depends on the number of games played'
      'and if they have actually attended. It also depends on the matches'
      'created and its calification. Moreover, after each match, a player'
      'can rate another player anonymously and randomly. Matches can also'
      'be rated by all players on a voluntary basis. In both cases the'
      'overall reputation of the players will be affected.'
    )
  )