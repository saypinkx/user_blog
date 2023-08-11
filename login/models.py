from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserModel(User):
    pass


class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_text = models.TextField()
    date = models.CharField(max_length=12, null=True)

