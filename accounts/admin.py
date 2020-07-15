from django.contrib import admin
from django.contrib.admin.models import LogEntry



# Register your models here.
from .models import *
from accounts.models import Entry, BlackList
from accounts.forms import EntryForm

# Register your models here.
from django.conf.urls.static import static

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'action_time', 'content_type', 'action_flag','change_message')
    search_fields = [
        'object_repr',
        'change_message'
    ]

    # keep only view permission
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
admin.site.register(LogEntry, LogEntryAdmin)


class EntryAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Number of Images', {
            'fields': ('Location_Name','locations','emergencycontacts','equipment_details','Agent_Company','agent_details','base_details','notice_period',
                       'support_craft_details','Provider_Company','tug_provider_details','area_details','navigational_hazards','met_ocean_conditions',
                       'environmental_details','degrees_latitude', 'minutes_latitude','seconds_latitude','degrees_longitude', 'minutes_longitude',
                       'seconds_longitude', 'STS_Latitude','STS_Longitude','number_of_images',),
            'classes': ('predefined',)
        }),
        (None, {
            'fields': (('Image1'),),
            'classes': ('oneimage',)
        }),


        (None, {
            'fields': (('Image2'),),
            'classes': ('twoimages',)
        }),

        (None, {
            'fields': (('Image3'),),
            'classes': ('threeimages',)
        }),

        (None, {
            'fields': (('Image4'),),
            'classes': ('fourimages',)
        }),

        (None, {
            'fields': (('Image5'),),
            'classes': ('fiveimages',)
        })
    )

    form = EntryForm

    class Media:
        js = ('//ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js', 'accounts/js/base.js',)

admin.site.register(Entry, EntryAdmin)
admin.site.register(BlackList)
