from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.db.models import Avg

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}'


class Blog(models.Model):
    user = models.ForeignKey( User , on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL , null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True , blank=True , unique=True)
    banner_image = models.ImageField(upload_to='blog.images/' , null=True , blank=True)
    views = models.IntegerField(null=True , blank=True)
    desciption = RichTextField(null=True , blank=True)
    image_1 = models.ImageField(upload_to='blog.images/' , null=True , blank=True)
    image_2 = models.ImageField(upload_to='blog.images/' , null=True , blank=True)
    image_3 = models.ImageField(upload_to='blog.images/' , null=True , blank=True)
    created_at = models.DateField(auto_now_add=True)
    autor = models.CharField(max_length=50 ,null=True,blank=True)
    image_autor = models.ImageField(upload_to='blog.images/', null=True,blank=True)
    position = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("single", kwargs={"slug": self.slug}) # struktura shunaqa yoziladi 
                                    
    @property
    def mid_rate(self):
        result = Rate.objcts.filter(blog_id=self.id).aaggregate(avarage=Avg('rate'))
        return result

class Rate(models.Model):
    RATING = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    blog =  models.ForeignKey(Blog , on_delete=models.CASCADE , null=True , related_name="rate_blogs")
    name = models.CharField(max_length=50 , default="Unknown")
    rate = models.IntegerField(choices=RATING , default=0)
    comment = models.TextField(null=True , blank=True)


class Subscribtion(models.Model):
    email = models.EmailField(null=True , blank=True)

    def __str__(self):
        return self.email