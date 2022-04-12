from email.policy import default
from django.db import models


class Pokemon(models.Model):
    '''Вид покемона'''

    title = models.CharField('Имя (рус.)', max_length=200)
    title_en = models.CharField('Имя (анг.)', max_length=200, default='')
    title_jp = models.CharField('Имя (яп.)', max_length=200, default='')
    image = models.ImageField('Изображение', upload_to='pokeimgsp', null=True)
    description = models.TextField('Описание', default='Этот покемон еще не описан')
    previous_evolution = models.ForeignKey(
        "self", 
        verbose_name='Эволюционирует из покемона',
        on_delete=models.SET_NULL, 
        related_name='next_evolution',
        null=True)


    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    '''Особь-покемон'''

    pokemon = models.ForeignKey(Pokemon, verbose_name='Вид покемона', on_delete=models.CASCADE)
    lat = models.FloatField('Координата по широте')
    lon = models.FloatField('Координата по долготе')
    appearance_at = models.DateTimeField('Дата появления', default=None, null=True)
    disappearance_at = models.DateTimeField('Дата исчезновения', default=None, null=True)
    level = models.IntegerField('Уровень', default=1)
    health = models.IntegerField('Здоровье', default=1)
    strength = models.IntegerField('Атака', default=1)
    defence = models.IntegerField('Защита', default=1)
    stamina = models.IntegerField('Выносливость', default=1)


    def __str__(self):
            return f'{self.pokemon.title} ({self.level} ур.)'
    