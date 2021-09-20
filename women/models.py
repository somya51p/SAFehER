from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Signup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    contact = models.CharField(max_length=10,null=True)
    role = models.CharField(max_length=15,null=True)

    # def __str__(self):
    #     return self.user.username


class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    uploadingdate = models.CharField(max_length=10,null=True)
    reportfile = models.FileField(null=True)
    filetype = models.CharField(max_length=30,null=True)
    description = models.CharField(max_length=300,null=True)
    status = models.CharField(max_length=30,null=True)

    # def __str__(self):
    #     return self.signup.user.username+" "+self.status


class Magazines(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    uploadedate = models.CharField(max_length=10,null=True)
    magazinesfile = models.FileField(null=True)
    magazinestype = models.CharField(max_length=30,null=True)
    description = models.CharField(max_length=300,null=True)
    status = models.CharField(max_length=30,null=True)

    # def __str__(self):
    #     return self.signup.user.username+" "+self.status