from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=False)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.caption}"

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=300)
    image_name = models.CharField(max_length=50)
    date = models.DateField(auto_now=True, auto_now_add=False, null=False)
    slug = models.SlugField(unique=True)
    content = models.TextField(max_length=2000)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="post")
    tags = models.ManyToManyField(Tag)
