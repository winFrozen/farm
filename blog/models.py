from django.db import models

# Create your models here.
class Farmers(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='Farmers/img')

class Blogs(models.Model):
    date = models.DateField()
    bio = models.TextField()
    img = models.ImageField(upload_to='Farmers/img')

class Products(models.Model):
    price = models.IntegerField()
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    img = models.ImageField(upload_to='Farmers/img')

    def get_absolute_url(self):
        return reverse("productdetailview", args=[self.slug])

    def __str__(self):
        return self.name


class Commenters(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    img = models.ImageField(upload_to='Commenters/img')


class Aboutus(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='Aboutus/img')

class Features(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='Features/img')

    def get_absolute_url(self):
        return reverse("featuresdetail", args=[self.slug])

    def __str__(self):
        return self.name

class Banner(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    img = models.ImageField(upload_to='Banner/img')


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    massage = models.TextField()

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email






