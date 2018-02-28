from django.db import models
import datetime as dt

class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Images(models.Model):
    image = models.ImageField(upload_to = 'images/', null = True)
    location = models.ForeignKey(Location, null=True)
    name = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True, null=True)
    descripton = models.TextField()
    # category = models.ManyToManyField(categories)
  

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_title(cls, search_term):
        gallery = cls.objects.filter(descripton__icontains=search_term)
        return gallery


class categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


