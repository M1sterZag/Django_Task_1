from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField()
    is_done = models.BooleanField(default=False)
    priority = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    