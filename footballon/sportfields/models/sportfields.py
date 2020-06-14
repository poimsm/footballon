# Django
from django.db import models

# Utilities
from footballon.utils.models import FootballonModel

class SportField(FootballonModel):
  """SportField model.

  Sports fields can generate weekly hours available for users
  to book and thus creating new football matches.

  Users can search fields ordered by distance and with
  available hours on the day they are looking for.
  """

  user = models.ForeignKey(
    'users.User',
    on_delete=models.CASCADE,
    help_text='This is the user who has registered and owns the field'
  )
  profile = models.ForeignKey(
    'users.Profile',
    on_delete=models.CASCADE,
    help_text='This is the profile of the user who owns the field'
  )

  name = models.CharField('field name', max_length=140)
  address = models.CharField('field address', max_length=255)

  latitude = models.FloatField()
  longitude = models.FloatField()

  logo = models.ImageField(
    'Sportfield logo',
    upload_to='sportfields/logos/',
    null=False
  )


