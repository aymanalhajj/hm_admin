from django.db import models


class UserType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class UserAccount(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    third_name = models.CharField(max_length=100)
    fourth_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.ForeignKey(UserType, on_delete=models.DO_NOTHING)

