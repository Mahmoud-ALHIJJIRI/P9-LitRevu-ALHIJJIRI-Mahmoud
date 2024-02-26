from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings


class Ticket(models.Model):
    title = models.CharField(max_length=128, verbose_name="Title")
    description = models.TextField(max_length=2048, blank=True, verbose_name="Description")
    image = models.ImageField(
        null=True, blank=True, verbose_name="Image", upload_to="images/")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Time created")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    headline = models.CharField(max_length=128, verbose_name="Titre")
    body = models.TextField(max_length=8192, blank=True, verbose_name="Commentaire")
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Time created")

    def __str__(self):
        return self.headline
