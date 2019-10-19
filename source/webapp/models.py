from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.question


class Choice(models.Model):
    option = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    poll = models.ForeignKey('Poll', related_name='poll_choice', on_delete=models.PROTECT, null=True,
                             blank=True, verbose_name='Опрос')

    def __str__(self):
        return self.option
