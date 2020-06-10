from django.db import models
from footballon.utils.models import FootballonModel

class Gallery(FootballonModel):
  sport_field = models.ForeignKey('fields.SportField', on_delete=models.CASCADE)
  picture = models.ImageField(
    'Gallery picture',
    upload_to='fields/pictures/',
    blank=True,
    null=True
  )
  