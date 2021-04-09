from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Signup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    contact = models.CharField(max_length=10,null=True)
    role = models.CharField(max_length=15,null=True)

    # def __str__(self):
    #     return self.user.username