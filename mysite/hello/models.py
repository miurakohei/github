from django.db import models


class Hello(models.Model):
    your_name=models.CharField(max_length=10)

    def __str__(self):
        return "<{0}".format(self.your_name)

"""
class Customer(models.Model):
    last_name=CharField(max_length=20)
    first_name=CharField(max_length=20)
    email_address=EmailField(max_length=255,unique=True)
    memo=TextField(null=True)
"""
