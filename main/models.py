from django.db import models


class Skill(models.Model):
    code = models.CharField(max_length=10, unique=True, verbose_name='Код навыка')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f"{self.code} - {self.description}"


class AgeGroup(models.Model):
    """Возрастные ступени (III, IV, V и т.д.)"""
    code = models.CharField(max_length=10, unique=True, verbose_name='Код ступени')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Возрастная ступень'
        verbose_name_plural = 'Возрастные ступени'

    def __str__(self):
        return str(self.code)


class Season(models.Model):
    """Времена года доступности маршрута"""
    name = models.CharField(max_length=20, unique=True, verbose_name='Сезон')

    class Meta:
        verbose_name = 'Сезон'
        verbose_name_plural = 'Сезоны'

    def __str__(self):
        return str(self.name)


class Route (models.Model):
    SKILL_CHOICES = (
        ('1', 'Установка палатки'),
        ('2', 'Разжигание костра'),
        ('3', 'Преодоление препятствий'),
        ('4', 'Вязка узлов'),
        ('5', 'Ориентирование'),
        ('6', 'Первая помощь'),
        ('7', 'Экологические навыки'),
        ('8', 'Выживание'),
        ('9', 'Видовые/возрастные навыки'),
    )

    # Основные поля
    name = models.CharField(max_length=150, verbose_name='Название')
    age_groups = models.ManyToManyField(AgeGroup, verbose_name='Возрастные ступени')
    distance = models.FloatField(verbose_name='Протяженность (км)')
    duration = models.FloatField(verbose_name='Продолжительность (в часах)')
    transportation_method = models.CharField(
        max_length=50,
        choices=[
            ('пеший', 'Пеший'),
            ('велосипедный', 'Велосипедный'),
            ('лыжный', 'Лыжный'),
            ('водный', 'Водный'),
        ],
        verbose_name='Способ передвижения'
    )
    cost = models.IntegerField(default=0, verbose_name='Стоимость (руб)')
    event_dates = models.TextField(verbose_name='Даты проведения', blank=True, null=True)
    seasons = models.ManyToManyField(Season, verbose_name='Сезоны доступности')
    skills = models.ManyToManyField(Skill, verbose_name='Проверяемые навыки')
    
    # Контактные данные
    organizer_name = models.CharField(max_length=100, verbose_name='ФИО организатора', blank=True, null=True)
    organizer_phone = models.CharField(max_length=50, verbose_name='Телефон', blank=True, null=True)
    organizer_email = models.EmailField(verbose_name='Почта', blank=True, null=True)
    organization = models.TextField(verbose_name='Организация', blank=True, null=True)

    # Данные о маршруте + карты
    route_passport = models.URLField(verbose_name='Паспорт маршрута', blank=True, null=True)
    image = models.ImageField(upload_to='routes_images', verbose_name='Изображение', blank=True, null=True)
    map_link = models.URLField(verbose_name='Ссылка на карту', blank=True, null=True)

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
        ordering = ('id',)

    def __str__(self):
        return str(self.name)
