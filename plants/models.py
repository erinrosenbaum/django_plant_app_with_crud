from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.urls import reverse

class Genus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "genus"

class Use(models.Model):
    use = models.CharField(max_length=50)

    def __str__(self):
        return self.use

class Plant(models.Model):
    species_name = models.CharField(max_length=50)
    common_name = models.CharField(max_length=50)
    genus = models.ForeignKey(Genus, on_delete=models.CASCADE)
    uses = models.ManyToManyField(Use)

    def __str__(self):
        return self.species_name

    class Meta:
        ordering = ('species_name',)

    def get_absolute_url(self):
        return reverse('plant_detail', args=[str(self.id)])
