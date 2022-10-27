from django.db import models
from django.utils.timezone import now


class Customers(models.Model):

    class Status(models.TextChoices):
        ACTIVE = 'Ativo'
        DISABLED = 'Desativado'

    name = models.CharField('Nome', max_length=180, null=False, blank=False)
    last_name = models.CharField('Sobrenome', max_length=180, null=False, blank=False)
    email = models.CharField('Email', max_length=180, null=False, blank=False)
    phone = models.CharField('Telefone', max_length=180, null=False, blank=False)
    cpf = models.CharField('CPF', max_length=180, null=False, blank=False)
    address = models.CharField('Endereço', max_length=180, null=False, blank=False)
    date_registration = models.DateTimeField(default=now)
    status = models.CharField(choices=Status.choices, max_length=180, null=False, blank=False)

