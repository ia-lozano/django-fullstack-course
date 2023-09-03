from django.db import models
from django.urls import reverse

# Create your models here.
class Console(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    emulator = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("crud_app:detail", kwargs={"pk": self.pk})

class Game(models.Model):
    name = models.CharField(max_length=50)
    release_year = models.PositiveBigIntegerField()
    console = models.ForeignKey(Console, related_name='games', on_delete=models.CASCADE)

    def __str__(self):
        return self.name