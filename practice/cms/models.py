from django.db import models


class User(models.Model):
    """顧客"""
    name=models.CharField('氏名',max_length=255)
    post=models.CharField('郵便番号',max_length=255)
    address=models.CharField('住所',max_length=255)

    def __str__(self):
        return self.name

