# app/blog/models.py

# Import django modules
from django.db import models
from django.utils.text import slugify

# MODEL: Tag
class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        return super(Tag, self).save(*args,**kwargs)

    def __str__(self):
        return self.name


# MODEL: Post
class Post(models.Model):
    title =  models.CharField(max_length=200)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    tags = models.ManyToManyField(Tag, blank=True, related_name='post_based_tag')
    view_count=models.IntegerField(null=True, blank=True)