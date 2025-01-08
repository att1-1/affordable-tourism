from django.db import models

class Routes(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    level = models.PositiveIntegerField(default=0, verbose_name='Уровень')
    duration = models.FloatField(verbose_name='Продолжительность')
    distance = models.FloatField(verbose_name='Протяженность в км')
    transportation_method = models.CharField(max_length=50, verbose_name='Способ передвижения')
    cost = models.IntegerField(default=0, verbose_name='Стоимость')
    event_date = models.DateField(verbose_name='Дата проведения')
    organizing_agency = models.TextField(blank=True, null=True, verbose_name='Проводящая организация')
    contact_info = models.TextField(verbose_name='Контактные данные')
    skill_name = models.TextField(verbose_name='Название навыка')
    route_passport = models.URLField(verbose_name='Ссылка на паспорт маршрута')
    # Поля таблицы для карты (изоборажение и ссылка на маршрут)
    map_link = models.URLField(verbose_name='Ссылка на карту маршрута')
    image = models.ImageField(upload_to='main_images', blank=True, null=True, verbose_name='Изображение маршрута')


    class Meta:
        db_table = 'route'
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
        ordering = ('id',)

    def __str__(self):
        return f'Маршрут уровня {self.level}'
