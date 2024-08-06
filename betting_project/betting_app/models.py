from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Bet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bets')
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
