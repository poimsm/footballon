from django.db import models
from footballon.utils.models import FootballonModel

class Profile(FootballonModel):
  user = models.OneToOneField('users.user', on_delete=models.CASCADE)
  picture = models.ImageField(
    'profile picture',
    upload_to='users/pictures',
    blank=True,
    null=True
  )
  #stats
  matches_played = models.PositiveIntegerField(default=0)
  matches_offered = models.PositiveIntegerField(default=0)
  reputation = models.FloatField(
    default=5.0,
    help_text=''
  )