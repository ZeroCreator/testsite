from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbouse_name='Наименование')
    content = models.TextField(blank=True, verbouse_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbouse_name='Дата публикации')
    update_at = models.DateTimeField(auto_now=True, verbouse_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbouse_name='Фото')
    is_published = models.BooleanField(default=True, verbouse_name='Опубликовано')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['cteated_at']


