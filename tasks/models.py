from django.db import models

# Create your models here.
class Task(models.Model):
    PRIORITIES = {
        "H": "Hight",
        "M": "Medium",
        "L": "Low"
    }
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    is_done = models.BooleanField(default=False)
    priority = models.CharField(max_length=1, choices=PRIORITIES)
    