from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

admin.site.register(Session)
admin.site.register(Participant)
admin.site.register(Booking)
admin.site.register(Speaker)
admin.site.register(Ticket)
admin.site.register(Notification)
admin.site.register(Review)


@admin.register(Conference)
class ProductAdmin(TranslationAdmin):
    list_display = ("title", 'description')
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }