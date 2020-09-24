from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title   = models.CharField(max_length=120)#msx_length required
    content = models.TextField()
    active  = models.BooleanField(default=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)

    def get_absolute_url(self):
        return reverse("article-detail",kwargs={"id":self.id})#f"/products/{self.id}"


    
# Create your models here.
