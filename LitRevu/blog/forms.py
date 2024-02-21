from django import forms
from django.urls import reverse_lazy
from . import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ["title", "description", "image"]
        success_url = reverse_lazy("blog:flux")
