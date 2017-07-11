from django.db import models


class Laserapp (models.Model):
    name = models.CharField('Name', max_length=30)
    desc = models.TextField('Description')
    price = models.FloatField('Price')

    class Meta:
        verbose_name = 'Laser cutting software'
        verbose_name_plural = 'Laser cutting softwares'

    def __str__(self):
        return self.name
