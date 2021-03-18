from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='blogs/images/')
    date = models.DateField()

    def __str__(self):
        return self.title

