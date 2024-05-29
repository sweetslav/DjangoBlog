from django.db import models
from django.utils import timezone


class Coin(models.Model):
    time = models.DateTimeField(default=timezone.now)
    side = models.CharField(max_length=10)

    def __str__(self):
        return f'Side: {self.side}\nTime: {self.time.strftime("%Y-%m-%d %H:%M:%S")}\n'

    @staticmethod
    def get_last_results():
        values = Coin.objects.all().order_by('-time')[:5]
        return values
