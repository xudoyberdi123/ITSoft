from django.db import models

# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    content = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    is_main = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.content)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.content


class Project(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    img = models.ImageField()

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    img = models.ImageField()

    def __str__(self):
        return self.title


class ServicesUslugi(models.Model):
    service = models.ForeignKey(Services, on_delete=models.SET_NULL, null=True)
    uslugi = models.CharField(max_length=512)

    def __str__(self):
        return self.uslugi


class Partner(models.Model):
    logo = models.ImageField(upload_to='partners/')
    name = models.CharField(max_length=128)
    social = models.CharField(max_length=256)

    def __str__(self):
        return self.name
