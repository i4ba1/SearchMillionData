from django.db import models


# Create your models here.
class zztemp_codinghw2(models.Model):
    text1 = models.TextField(default='', blank=False)
    text2 = models.TextField(default='', blank=False)
