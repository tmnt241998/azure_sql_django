from datetime import timezone
from django.db import models

# Create your models here.


class Store(models.Model):
    store_id = models.IntegerField(unique=True)
    store_location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.store_id} - {self.store_location}"
