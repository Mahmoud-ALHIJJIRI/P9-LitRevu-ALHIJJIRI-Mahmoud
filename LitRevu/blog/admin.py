from django.contrib import admin
from .models import Ticket


# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "image", "time_created", "user")

    def ticket_title(self, obj):
        return obj.ticket.title

    def ticket_image(self, obj):
        return obj.ticket.image

    def ticket_description(self, obj):
        return obj.ticket.description


admin.site.register(Ticket, TicketAdmin)
