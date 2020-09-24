from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

#from django.conf import settings
# Create your models here.
class Profile(models.Model):
    user= models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    username = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    profile_pic=models.ImageField(default="coffee.jpg",null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    #User.userid = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)


    def __str__(self):
        return str(self.username)

    def get_absolute_url(self):
        return reverse("profile-detail",kwargs={"id":self.id})#f"/products/{self.id}"

    @property
    def relative_path(self):
        return os.path.relpath(self.path, settings.MEDIA_ROOT)