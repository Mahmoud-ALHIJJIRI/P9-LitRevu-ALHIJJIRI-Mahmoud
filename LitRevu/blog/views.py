from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib import messages


@login_required
def home(request):
    return render(request, 'blog/home.html')


@login_required
def create_ticket(request):
    if request.method == "POST":
        # Create an instance of the ticket form with the submitted data
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            # Set the user for the ticket
            ticket.user = request.user
            ticket.save()

            messages.success(request, "Ticket créé avec succès.")

            return redirect("blog:flux")
        else:
            messages.error(
                request,
                "Erreur lors de la création du ticket. Veuillez vérifier le formulaire.",
            )
    else:
        # If the request is a GET request (the user is loading the page),
        # create an instance of an empty ticket form
        form = forms.TicketForm()

    # Pass the ticket form to the template
    context = {
        "form": form,
    }

    return render(request, "blog/create_ticket.html", context)

