from django.db import models

# Create your models here.

class Category(models.Model):
  title = models.CharField(max_length=100, db_index=True)
  url = models.SlugField(max_length=100, db_index=True)

  def __str__(self):
    return self.title


class Author(models.Model):
  name = models.CharField(max_length=100, db_index=True)
  email = models.CharField(max_length=100, db_index=True)
  url = models.SlugField(max_length=100, db_index=True)
  body = models.TextField()
  descritpion = models.TextField()

  def __str__(self):
    return self.name


class Post(models.Model):
  title = models.CharField(max_length=100, unique=True)
  url = models.SlugField(max_length=100, unique=True)
  body = models.TextField()
  descritpion = models.TextField()
  date = models.DateField(db_index=True, auto_now_add=True)
  category = models.ForeignKey('nblog.Category')
  author = models.ForeignKey('nblog.Author')  

  def __str__(self):
    return self.title

