from django.db import models


class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
    info = models.TextField()
    img = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name