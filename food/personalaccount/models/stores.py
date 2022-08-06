from django.db import models




class Store (models.Model):
    name = models.CharField(max_length=70, verbose_name='Название магазина')
    users = models.ManyToManyField(
        to='users.User', related_name='users_store',
        verbose_name='Работники магазина',
    )
    description =models.TextField(verbose_name='Описание магазина')
    # status = models.CharField(max_length=30, choices=Status.choices)
    time_to_order = models.DateTimeField(
        verbose_name='Дата начала работы', auto_now_add=True
    )


    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return f'№:{self.id}, Магазин:{self.status}, работает с :{self.time_to_order}'