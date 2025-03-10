from django.db import models


class TeleSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Токен')
    tg_chat = models.CharField(max_length=100, verbose_name='Чат айди')
    tg_message = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.tg_chat

    class Meta:
        verbose_name = 'настройку'
        verbose_name_plural = 'Настройки'
# Create your models here.
