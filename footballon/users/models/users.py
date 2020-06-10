# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utils
from footballon.utils.models import FootballonModel

class User(FootballonModel, AbstractUser):

  email = models.EmailField(
    'email address',
    unique=True,
    error_messages={
      'unique': 'A user with that email already exists.'
    }
  )
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  is_field_owner = models.BooleanField(
    'field owner',
    default=False,
    help_text='Set to true when the user is the owner of a football field'
  )