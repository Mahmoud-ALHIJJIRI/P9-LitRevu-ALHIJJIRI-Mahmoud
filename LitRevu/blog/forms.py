from django import forms

class CreateTicketForm(forms.ModelForm):
    class Meta:
        model =