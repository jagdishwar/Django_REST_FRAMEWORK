from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)