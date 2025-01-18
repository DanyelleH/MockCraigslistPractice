from django.db import models
from datetime import datetime
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, default="Miscellaneous")
    

class Post(models.Model):
    content = models.CharField(max_length=500, default='post description here')
    posting_date = models.DateField(default=datetime.now)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='posts')