from django.db import models


class Post(models.Model):
    text = models.TextField()

    # Parodo pirmus 50 simboliu
    def __str__(self):
        return self.text[:50]
