from django.db import models
from django.utils import timezone


NULLABLE = {'blank': True, 'null': True}


class Contact(models.Model):
    email = models.EmailField(verbose_name='email')
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    house_number = models.CharField(max_length=20, verbose_name='номер дома')

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"

    class Meta:
        verbose_name = 'контактная информация'
        verbose_name_plural = 'контакты'


class NetworkNode(models.Model):
    NODE_TYPES = [
        ('Factory', 'Factory'),
        ('Retail Network', 'Retail Network'),
        ('Individual Entrepreneur', 'Individual Entrepreneur'),
    ]

    name = models.CharField(max_length=200, verbose_name='название')
    node_type = models.CharField(choices=NODE_TYPES, verbose_name='тип узла')
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, verbose_name='контакты')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='поставщик')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='задолженность')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='время создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'звено'
        verbose_name_plural = 'звенья'


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    model = models.CharField(max_length=100, verbose_name='модель')
    release_date = models.DateField(verbose_name='дата выхода товара')
    company = models.ForeignKey(NetworkNode, on_delete=models.CASCADE, verbose_name='компания реализатор')

    def __str__(self):
        return f"{self.title} - {self.model}"

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
