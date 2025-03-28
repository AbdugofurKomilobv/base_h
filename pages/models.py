from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=128)
    text = models.TextField()

    def __str__(self):
        return self.name
