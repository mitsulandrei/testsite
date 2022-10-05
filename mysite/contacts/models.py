from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=150, blank=True, verbose_name='Имя')
    job_title = models.CharField(max_length=150, blank=True, verbose_name='Должность')
    photo = models.ImageField(upload_to='contacts_photo/%Y/%m/', blank=True, verbose_name='Фото')
    number = models.CharField(max_length=50,blank=True, verbose_name='Номер телефона')
    mail = models.CharField(max_length=100,blank=True, verbose_name='Электронная почта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Статус публикации')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория контактов', null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
        ordering = ['name']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория контактов')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория Контактов'
        verbose_name_plural = 'Категории контактов'
        ordering = ['title']