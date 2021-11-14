from django.db import models

# Create your models here.
class skills(models.Model):
    name_skills = models.CharField(max_length=100)
    
