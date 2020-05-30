from django.db import models

class PreLaunchSignup(models.Model):
    email = models.CharField(max_length=200)
    signup_date = models.DateTimeField('date published')
