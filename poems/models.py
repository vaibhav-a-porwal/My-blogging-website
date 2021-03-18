from django.db import models

class Poem(models.Model):
    image = models.ImageField(upload_to='poems/images/')
