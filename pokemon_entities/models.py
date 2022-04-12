from email.policy import default
from django.db import models


class Pokemon(models.Model):
    '''Вид покемона'''

    title = models.CharField('Имя (рус.)', max_length=200)
    title_en = models.CharField('Имя (анг.)', max_length=200, blank=True)
    title_jp = models.CharField('Имя (яп.)', max_length=200, blank=True)
    image = models.ImageField('Изображение', upload_to='pokeimgsp', null=True)
    description = models.TextField('Описание', default='Этот покемон еще не описан', blank=True)
    previous_evolution = models.ForeignKey(
        "self", 
        verbose_name='Эволюционирует из покемона',
        on_delete=models.SET_NULL, 
        related_name='next_evolution',
        null=True,
        blank=True)


    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    '''Особь-покемон'''

    pokemon = models.ForeignKey(
        Pokemon, 
        verbose_name='Вид покемона', 
        on_delete=models.CASCADE,
        related_name='entities')
    lat = models.FloatField('Координата по широте')
    lon = models.FloatField('Координата по долготе')
    appearance_at = models.DateTimeField('Дата появления', default=None, null=True, blank=True)
    disappearance_at = models.DateTimeField('Дата исчезновения', default=None, null=True, blank=True)
    level = models.IntegerField('Уровень', null=True, blank=True)
    health = models.IntegerField('Здоровье', null=True, blank=True)
    strength = models.IntegerField('Атака', null=True, blank=True)
    defence = models.IntegerField('Защита', null=True, blank=True)
    stamina = models.IntegerField('Выносливость', null=True, blank=True)


    def __str__(self):
            return f'{self.pokemon.title} [{self.lat} : {self.lon}]'
    