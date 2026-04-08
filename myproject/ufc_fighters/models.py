from django.db import models

class Fighter(models.Model):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    weight_class = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    created_ad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

