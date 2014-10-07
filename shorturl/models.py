from django.db import models

# Create your models here.
class urlObj(models.Model):
    original_url = models.CharField(max_length=200) # URL to shorten
    short_url = models.CharField(unique=True, max_length=200) # Shortened URL
    date_created = models.DateTimeField('Date Created')

   
    
