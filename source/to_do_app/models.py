from django.db import models


# Create your models here.
class ToDoParagraph(models.Model):
    STATUS_CHOICES = {
        ('new', 'Новая'),
        ('in_process', 'В процессе'),
        ('complete', 'Завершена')
    }
    title = models.CharField(max_length=400, blank=True, null=False, verbose_name='Задача')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='new', verbose_name='Статус задачи')
    completion_date = models.DateField(verbose_name='Дата выполнения', null=True)

    @classmethod
    def return_choices(cls):
        return cls.STATUS_CHOICES

