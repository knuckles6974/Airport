from django.db import models

class Iata(models.Model):
    name = models.CharField(max_length=7)

    class Meta:
        db_table = 'iatas'

class Icao(models.Model):
    name = models.CharField(max_length=7)
    
    class Meta:
        db_table = 'icaos'

class Airport(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=20, decimal_places=10, default=0.0)
    longitude = models.DecimalField(max_digits=20, decimal_places=10, default=0.0)
    elevation = models.IntegerField()
    tz = models.CharField(max_length=20)
    icao = models.ForeignKey(Icao, on_delete=models.CASCADE)
    iata = models.ForeignKey(Iata, on_delete=models.CASCADE)

    class Meta:
        db_table = 'airports'