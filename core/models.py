from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=155, verbose_name='Заголовок')
    text = models.TextField(max_length=1000, verbose_name='Текст')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_date']

    def __str__(self):
        return self.title

