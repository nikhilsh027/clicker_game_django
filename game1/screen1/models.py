from django.db import models
class GameScore(models.Model):
    score = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-score']

# Create your models here.
