from django.db import models

class Qoshiqchi(models.Model):
    ism = models.CharField(max_length=255)
    davlat = models.CharField(max_length=255)
    t_sana = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.ism

class Albom(models.Model):
    nom = models.CharField(max_length=255)
    sana = models.DateField()
    rasm = models.ImageField(blank=True, null=True)
    qoshiqchi = models.ForeignKey(Qoshiqchi, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom

class Jadval(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=255)
    davomiylik = models.DurationField()
    fayl = models.FileField(blank=True, null=True)
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom