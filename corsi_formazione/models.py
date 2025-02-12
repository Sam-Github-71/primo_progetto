from django.db import models

# Create your models here.

class Corso(models.Model):
    titolo = models.CharField(max_length=100)
    descrizione = models.TextField()
    data_inizio = models.DateField()
    data_fine = models.DateField()
    posti_disponibili = models.IntegerField()

    def __str__(self):
        return self.titolo + " " + self.descrizione + " " + self.data_inizio + " " + self.data_fine + " " + self.posti_disponibili