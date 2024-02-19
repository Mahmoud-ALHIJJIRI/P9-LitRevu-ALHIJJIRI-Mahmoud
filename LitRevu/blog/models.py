from django.db import models
from django.conf import settings


class Ticket(models.Model):
    title = models.CharField(max_length=128, verbose_name="Title")
    description = models.TextField(max_length=2048, blank=True, verbose_name="Description")
    image = models.ImageField(
        null=True, blank=True, verbose_name="Image", upload_to="images/")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Time created")
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
