from django.db import models

# Create your models here.
class task(models.Model):

    # id = 1, 2, 3, 4,
    content = models.CharField(max_length=140)
    posted_date = models.DateTimeField(auto_now_add=True)
