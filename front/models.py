from django.db import models

from django.contrib.postgres.fields import JSONField
from django_better_admin_arrayfield.models.fields import ArrayField


# Create your models here.
class ArticleKind(models.Model):
    kind = models.CharField(max_length=100, verbose_name="Тип новости")

    class Meta:
        ordering = ["pk"]
        verbose_name = "Тип новости"
        verbose_name_plural = "2 - Типы новости"

    def __str__(self):
        return self.kind


class Article(models.Model):
    kind = models.ForeignKey('ArticleKind', null=True, blank=True, default=None, on_delete=models.SET_DEFAULT,
                             verbose_name="Тип новости")
    date_publish = models.DateTimeField(verbose_name="Дата публикации новости")
    title = models.CharField(max_length=250, verbose_name="Заголовок новости")
    cover = models.FileField(upload_to='images/covers/', blank=True, verbose_name="Обложка новости")
    content = models.TextField(blank=True, verbose_name="Содержание (текст) новости")
    videolink = models.TextField(null=True, blank=True, verbose_name="Идентификатор в ссылке на видео Youtube")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "1 - Новости"

    def __str__(self):
        return f'{self.kind} -  {self.title} - {self.date_publish}'


class APhoto(models.Model):
    article = models.ForeignKey('Article', null=True, blank=True, default=None, on_delete=models.CASCADE,
                                verbose_name="Новости")
    photo = models.ImageField(upload_to='images/articles/', verbose_name="Фотографии (одна или несколько)")

    def __str__(self):
        return f'{self.photo.name}'


class Projects(models.Model):
    title = models.CharField(max_length=100, verbose_name="Наименование проекта")
    logo = models.ImageField(upload_to='images/logos/', blank=True,
                             verbose_name="Логотип (оптимальная высота 180px +-20px)")
    order = models.PositiveSmallIntegerField(verbose_name="Порядок отображения", null=True, blank=True, unique=True)
    short_description = models.TextField(null=True, blank=True, verbose_name="Краткое описание на главной")
    full_description = models.TextField(null=True, blank=True, verbose_name="Полное описание")
    photo_amount = models.PositiveSmallIntegerField(verbose_name="Количество отображаемых фото в разделе проекта", default=0)
    videolink = models.TextField(null=True, blank=True, verbose_name="Идентификатор в ссылке на видео Youtube")
    color = models.CharField(max_length=10, choices=(('1', 'Белый'), ('2', 'Синий')),
                             verbose_name="Фон карточки проекта на Главной")

    class Meta:
        ordering = ["order"]
        verbose_name = "Проект"
        verbose_name_plural = "5 - Проекты"

    def __str__(self):
        return f'{self.title}'


class Blagodarnosti(models.Model):
    year = models.CharField(max_length=4, verbose_name="Год - в формате 4 цифр")

    class Meta:
        ordering = ["-year"]
        verbose_name = "Благодарности"
        verbose_name_plural = "4 - Благодарности"

    def __str__(self):
        return f'{self.year}'


class BPhoto(models.Model):
    year = models.ForeignKey('Blagodarnosti', null=True, blank=True, default=None, on_delete=models.CASCADE,
                                verbose_name="Благодарности")
    photo = models.ImageField(upload_to='images/blagodarnosti/', verbose_name="Фотографии (одна или несколько)")

    def __str__(self):
        return f'{self.photo.name}'


class Documents(models.Model):
    title = models.TextField(verbose_name="Наименование файла на сайте")
    file = models.FileField(upload_to='files/', verbose_name="Файл")
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время добавления файла")

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "3 - Документы"

    def __str__(self):
        return f'{self.title}'


class Settings(models.Model):
    mailto = ArrayField(models.EmailField(), verbose_name="Почта, для уведомлений обратной связи")
    contact_phone = models.CharField(max_length=50, default='', blank=True, null=True,
                                     verbose_name="Телефон 'Контакты' на главной")
    contact_email = models.CharField(max_length=50, default='', blank=True, null=True,
                                     verbose_name="Email 'Контакты' на главной")
    contact_address = models.TextField(default='', blank=True, null=True,
                                       verbose_name="Адрес 'Контакты' на главной")
    contact_map = models.TextField(default='', blank=True, null=True, verbose_name="Ссылка на адрес в google maps")
    requisites = models.TextField(default='', blank=True, null=True, verbose_name="Реквизиты")
    banner_text = models.TextField(default='Добро пожаловать!', blank=True, null=True,
                                   verbose_name="Текст бегущей строки")
    about_text = models.TextField(default='', blank=True, null=True, verbose_name="Текст 'О Фонде' на главной")
    metadescr = models.TextField(default='', blank=True, null=True, verbose_name="Meta Description")
    metakeywords = models.TextField(default='', blank=True, null=True, verbose_name="Meta Keyword")
    default_newscover = models.ImageField(upload_to='images/covers/', blank=True,
                                          verbose_name="Обложка новости по умолчанию")
    default_videocover = models.ImageField(upload_to='images/covers/', blank=True,
                                           verbose_name="Обложка видео по умолчанию")
    ig = models.CharField(max_length=100, default='', blank=True, null=True,
                          verbose_name="Ссылка на аккаунт в Instagram")
    vk = models.CharField(max_length=100, default='', blank=True, null=True,
                          verbose_name="Ссылка на аккаунт в Вконтакте")
    ok = models.CharField(max_length=100, default='', blank=True, null=True,
                          verbose_name="Ссылка на аккаунт в Одноклассники")
    yt = models.CharField(max_length=100, default='', blank=True, null=True, verbose_name="Ссылка на аккаунт в Youtube")
    fb = models.CharField(max_length=100, default='', blank=True, null=True, verbose_name="Ссылка на аккаунт в Facebook")
    tw = models.CharField(max_length=100, default='', blank=True, null=True, verbose_name="Ссылка на аккаунт в Twitter")

    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "6 - Настройки"

    def __str__(self):
        return f'{self.mailto}'
