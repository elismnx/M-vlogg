from django.db import models

# Create your models here.

class Settings(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    number = models.CharField(max_length=100)
    hone_number = models.CharField(max_length=100)
    email = models.EmailField()
    pinterest = models.URLField(blank=True,null=True)
    twitter = models.URLField(blank=True,null=True)
    instagram = models.URLField(blank=True,null=True)
    google = models.URLField(blank=True,null=True)
    youtube = models.URLField(blank=True,null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'

class Books(models.Model):
    book_img = models.ImageField() 
    name = models.CharField(max_length=100)
    description = models.TextField()
    book_pdf = models.FileField(upload_to='book-pdf')

    def __str__(self):
        return self.name
    


class Podcast(models.Model):
    audio = models.FileField(upload_to='podcast/')
    title = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

class Video(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='video/')

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
