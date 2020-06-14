from django.db import models
from footballon.utils.models import FootballonModel

class Match(FootballonModel):
  """Match model.

  Users can create a new match or join an already created one.
  When a user reserves an hour in a sports field, a new match
  is automatically created.
  """

  sportfield = models.ForeignKey('sportfields.SportField', on_delete=models.CASCADE)
  players = models.ManyToManyField('users.User', through='matches.Player')

  hour = models.OneToOneField(
    'sportfields.Hour',
    on_delete=models.SET_NULL,
    help_text='Each match is related to a single hour.'
  )

  rating = models.FloatField(
    null=True,
    help_text='Average of all ratings that players have given to the match.'
  )

  spots_left = models.SmallIntegerField(
    default=10,
    help_text='Each match starts with 10 free spots for players to join in.'
  )

