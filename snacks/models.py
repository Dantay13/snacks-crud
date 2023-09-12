from django.db import models
from django.urls import reverse


class Snack(models.Model):
    title = models.CharField(max_length=255)
    purchaser = models.CharField(max_length=255)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('snack_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

