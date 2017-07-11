from django.db import models


class Laserapp (models.Model):
    name = models.CharField('Name', help_text='Name of your material', max_length=30, )
    desc = models.TextField('Description', help_text='Short description', null=True, blank=True,)
    price = models.FloatField('Price', help_text='Price of cutting', )
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name = 'Laser cutting software'
        verbose_name_plural = 'Laser cutting softwares'

    def __str__(self):
        return self.name

    def cap_name(self):
        return self.name.upper()
