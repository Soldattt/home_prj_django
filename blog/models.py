from django.db import models



class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='blog/image', blank=True, null=True, verbose_name='Превью')
    status = models.BooleanField(verbose_name='Признак публикации', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(verbose_name='Количество просмотров', default=0)


    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['title']

    def __str__(self):
        return f'Тайтл: {self.title}, дата создания: {self.created_at}, просмотров: {self.status}.'



