from django.db import models
from django.urls.base import reverse


class ProductManager(models.Manager):
    def update_price(self, k):
        self.get_queryset().all().update(price=k*models.F('price'))
    def get_queryset(self):
        return super().get_queryset().filter(price__gt=1)


class AllProductsManager(models.Manager):
    pass


class Brand(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Laserapp(models.Model):
    name = models.CharField('Name', help_text='Name of your material', max_length=30, )
    desc = models.TextField('Description', help_text='Short description', null=True, blank=True,)
    price = models.FloatField('Price', help_text='Price of cutting', )
    slug = models.SlugField(max_length=50, unique=True)
    brand = models.ForeignKey(Brand)

    class Meta:
        verbose_name = 'Laser cutting software'
        verbose_name_plural = 'Laser cutting softwares'

    def __str__(self):
        return self.name

    def cap_name(self):
        return self.name.upper()

    all_products = AllProductsManager()
    objects = ProductManager()

    def get_absolute_url(self):
        return reverse('laserapp:details', args=[self.slug])



    # for testing
class Notebook(models.Model):
    price = models.PositiveIntegerField()
    name = models.CharField(max_length=30)

    class Meta:
        abstract = True


class IBook(Notebook):
    ram = models.PositiveIntegerField()
    cpu = models.CharField(max_length=10)


class IIBook(IBook):
    sensor = models.CharField(max_length=10)
    # end of testing