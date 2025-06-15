from django.db import models
from django.contrib.auth.models import User

class FavoriteLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Користувач')
    city = models.CharField(max_length=100, verbose_name='Місто')
    country = models.CharField(max_length=100, verbose_name='Країна')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата додавання')

    class Meta:
        verbose_name = 'Улюблене місце'
        verbose_name_plural = 'Улюблені місця'
        unique_together = ['user', 'city', 'country']

    def __str__(self):
        return f"{self.city}, {self.country}"

class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Користувач')
    city = models.CharField(max_length=100, verbose_name='Місто')
    country = models.CharField(max_length=100, verbose_name='Країна')
    temperature = models.FloatField(verbose_name='Температура')
    description = models.CharField(max_length=200, verbose_name='Опис погоди')
    searched_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата пошуку')

    class Meta:
        verbose_name = 'Історія пошуку'
        verbose_name_plural = 'Історія пошуків'
        ordering = ['-searched_at']

    def __str__(self):
        return f"{self.city}, {self.country} - {self.searched_at.strftime('%d.%m.%Y %H:%M')}"
