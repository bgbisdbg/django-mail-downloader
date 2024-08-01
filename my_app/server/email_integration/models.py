from django.db import models


class EmailAccount(models.Model):
    PROVIDER_CHOICES = [
        ('gmail', 'Gmail'),
        ('yandex', 'Yandex'),
        ('mailru', 'Mail.ru'),
    ]
    provider = models.CharField(max_length=10, choices=PROVIDER_CHOICES)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)


class EmailMessage(models.Model):
    email_account = models.ForeignKey(EmailAccount, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    sent_date = models.CharField(max_length=50)  # Изменено на CharField
    received_date = models.CharField(max_length=50)  # Изменено на CharField
    body = models.TextField()
    attachments = models.JSONField(default=list)
