from django.db import models

# Create your models here.
class JobSearch(models.Model):
    date_started = models.DateField()
    date_ended = models.DateField()
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['date_started']
