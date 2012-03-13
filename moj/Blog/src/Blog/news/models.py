from django.db import models

class Artykul(models.Model):
    nazwa = models.CharField(max_length=45,verbose_name='Tytul Newsa')