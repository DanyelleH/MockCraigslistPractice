from django.db import models
import datetime
from datetime import date
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, default="Miscellaneous")
    
    def get_posts(self):
        return self.posts.all()

class Post(models.Model):
    title = models.CharField(max_length=255, null=True)
    content = models.CharField(max_length=500, default='post description here')
    posting_date = models.DateField(default=datetime.date.today)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='posts')