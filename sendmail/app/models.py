from django.db import models

class Car(models.Model):
    name=models.CharField(max_length=1000) 
    def __str__(self) -> str:
        return self.name
class Trailers(models.Model):
    name=models.CharField(max_length=1000) 
    def __str__(self) -> str:
        return self.name