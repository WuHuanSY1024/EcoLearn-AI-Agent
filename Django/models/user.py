from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now

class User(AbstractUser):
    points = models.IntegerField(default=0)
    joined_date = models.DateTimeField(default=now)

    def add_points(self, amount):
        if amount > 0:
            self.points += amount
            self.save()

    def redeem_points(self, amount):
        if amount > 0 and self.points >= amount:
            self.points -= amount
            self.save()
            return True
        return False

    def __str__(self):
        return f"{self.username} - Points: {self.points}"
