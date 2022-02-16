from django.db import models

# Create your models here.
class Restapi(models.Model):
    kod = models.CharField(max_length=255)
    
    def __str__(self):
        return  self.kod