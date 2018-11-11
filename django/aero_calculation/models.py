from django.db import models


class Section(models.Model):
    temperature = models.CharField(max_length=5)
    consumption = models.CharField(max_length=10)
    length = models.CharField(max_length=10)
    recommended_speed = models.CharField(max_length=10)
    coeff_roughness = models.CharField(max_length=10)

    def __str__(self):
        return self.temperature

    def set(self, str):
        elements = str.split(' ')
        self.temperature = elements[0]
        self.consumption = elements[1]
        self.length = elements[2]
        self.recommended_speed = elements[3]
        self.coeff_roughness = elements[4]
