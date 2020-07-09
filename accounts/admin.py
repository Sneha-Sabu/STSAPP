from django.contrib import admin


# Register your models here.
from .models import *
from accounts.models import Entry
from accounts.forms import EntryForm

# Register your models here.
from django.conf.urls.static import static



class EntryAdmin(admin.ModelAdmin):

    fieldsets = (
        ('Number of Images', {
            'fields': ('Location_Name','locations','emergencycontacts','equipment_details','Agent_Company','agent_details','base_details','notice_period','support_craft_details','Provider_company','tug_provider_details','area_details','navigational_hazards','met_ocean_conditions','environmental_details','number_of_images',),
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
