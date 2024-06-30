from django.db import models
from user.models import Account
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(Account,related_name='user',on_delete=models.CASCADE)
    medea = models.CharField(max_length=1000,default=None)
    text = models.CharField(max_length=10000,default=None)
    
