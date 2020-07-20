from __future__ import unicode_literals
from djongo import models
from django import forms
from multiselectfield import MultiSelectField
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, Textarea
import datetime
from django.utils import timezone



# Create your models here.

Cargoes_Permitted = ((1, 'Oil'),
                     (2, 'LPG'),
                     (3, 'Chemicals'),
                     (4, 'LNG'),
                     (5, 'All cargoes permitted'))


class Locations(models.Model):
    name = models.CharField(max_length=200, null=True)
    fendering_position = models.CharField(max_length=1000, null=True, blank=True)
    Cargos_permitted = MultiSelectField(choices=Cargoes_Permitted, max_choices=5, max_length=1000, null=True, blank=True )
    Type_of_operation = models.CharField(max_length=1000, null=True, blank=True)
    Depth_of_water = models.CharField(max_length=1000, null=True, blank=True)
    Approval_to_conduct_STS_issued_by = models.CharField(max_length=1000, null=True, blank=True)
    Approval_needed_prior_to_each_STS_operation = models.CharField(max_length=1000, null=True, blank=True)
    Vessel_sizes_permitted = models.CharField(max_length=1000, null=True, blank=True)
    Night_time_berthing_permitted = models.CharField(max_length=1000, null=True, blank=True)
    Is_local_piloting_assistance_required = models.CharField(max_length=1000, choices=[('Yes', 'Yes'), ('No', 'No')], null=True, blank=True)
    Local_piloting_additional_information = models.CharField(max_length=1000, null=True, blank=True)
    Are_tugs_required = models.CharField(max_length=1000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    locations_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Region(models.Model):
    Name = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.Name

class EmergencyContacts(models.Model):
    Oil_Spill_Responders = models.CharField(max_length=1000, null=True, blank=True)
    Local_Emergency_Medical_Assistance = models.CharField(max_length=1000, null=True, blank=True)
    Police = models.CharField(max_length=1000, null=True, blank=True)
    Coast_Guard = models.CharField(max_length=1000, null=True, blank=True)
    Fire_fighting = models.CharField(max_length=1000, null=True, blank=True)

class Equipment_Details(models.Model):
    Primary_Fenders = models.CharField(max_length=1000, null=True, blank=True)
    Secondary_Fenders = models.CharField(max_length=1000, null=True, blank=True)
    Fender_Moorings = models.CharField(max_length=1000, null=True, blank=True)
    Rubber_Hoses = models.CharField(max_length=1000, null=True, blank=True)
    Composite_Hoses = models.CharField(max_length=1000, null=True, blank=True)

class Agent_Details(models.Model):
    Agent_Company = models.CharField(max_length=1000, null=True, blank=True)
    Agent_Contact = models.CharField(max_length=1000, null=True, blank=True)
    Fees_to_be_incurred_for_STS_Operations = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

class Base_Details(models.Model):
    Base_Location = models.CharField(max_length=1000, null=True, blank=True)
    Storage_Space = models.CharField(max_length=1000, null=True, blank=True)
    Security_Arrangements = models.CharField(max_length=1000, null=True, blank=True)
    Closest_Airport = models.CharField(max_length=1000, null=True, blank=True)
    Local_taxi_firms = models.CharField(max_length=1000, null=True, blank=True)
    Accommodation = models.CharField(max_length=1000, null=True, blank=True)
    Base_facilities = models.CharField(max_length=1000, null=True, blank=True)

class Notice_Period(models.Model):
    Notice_Period = models.CharField(max_length=1000, null=True, blank=True)
    Documentation_Requirements = models.CharField(max_length=1000, null=True, blank=True)

class Support_Craft_Details(models.Model):
    Vessel_Name = models.CharField(max_length=1000, null=True, blank=True)
    Support_Craft_Owner = models.CharField(max_length=1000, null=True, blank=True)
    Telephone = models.CharField(max_length=1000, null=True, blank=True)

class Tug_Provider_Details(models.Model):
    Tug_Provider_Company = models.CharField(max_length=1000, null=True, blank=True)
    Tug_Provider_Contact = models.CharField(max_length=1000, null=True, blank=True)
    Tug_Provider_Vessel_Name = models.CharField(max_length=1000, null=True, blank=True)

class Area_Details(models.Model):
    Location_under_the_control_of_authorities = models.CharField(max_length=1000, null=True, blank=True)
    Current_port_security_level = models.CharField(max_length=1000, null=True, blank=True)
    What_is_considered_port_limits = models.CharField(max_length=1000, null=True, blank=True)
    What_is_considered_international_waters = models.CharField(max_length=1000, null=True, blank=True)
    Distance_from_support_base = models.CharField(max_length=1000, null=True, blank=True)
    Transit_time_from_shore_to_STS_location = models.CharField(max_length=1000, null=True, blank=True)
    Size_of_transfer_area = models.CharField(max_length=1000, null=True, blank=True)
    Does_the_area_have_a_large_enough_run_in_area = models.CharField(max_length=1000, null=True, blank=True)
    Is_the_transfer_area_sheltered = models.CharField(max_length=1000, null=True, blank=True)
    Regulations_to_be_complied_during_the_operation = models.CharField(max_length=1000, null=True, blank=True)
    Nature_of_seabed = models.CharField(max_length=1000, null=True, blank=True)
    Average_depth_of_water = models.CharField(max_length=1000, null=True, blank=True)
    STS_location_suitable_for_anchoring = models.CharField(max_length=1000, null=True, blank=True)
    Any_other_service_provider_in_the_same_vicinity = models.CharField(max_length=1000, null=True, blank=True)

class Navigational_Hazards(models.Model):
    Local_marine_activity = models.CharField(max_length=1000, null=True, blank=True)
    Any_physical_limitations_on_vessel_size = models.CharField(max_length=1000, null=True, blank=True)
    Distance_from_land = models.CharField(max_length=1000, null=True, blank=True)
    Any_other_navigational_hazards_in_the_area = models.CharField(max_length=1000, null=True, blank=True)

class Met_Ocean_Conditions(models.Model):
    Prevailing_winds = models.CharField(max_length=1000, null=True, blank=True)
    Predominant_current = models.CharField(max_length=1000, null=True, blank=True)
    Average_wave_height = models.CharField(max_length=1000, null=True, blank=True)
    Average_swell_height_and_period = models.CharField(max_length=1000, null=True, blank=True)
    What_is_the_tidal_range_if_applicable = models.CharField(max_length=1000, null=True, blank=True)
    Location_subject_to_restrictive_Met_conditions = models.CharField(max_length=1000, null=True, blank=True)
    STS_Location_covered_by_forecasting_service = models.CharField(max_length=1000, null=True, blank=True)

class Environmental_Details(models.Model):
    Location_adjacent_to_any_public_sensitive_areas = models.CharField(max_length=1000, null=True, blank=True)
    Environmental_bodies_to_be_advised_of_operations = models.CharField(max_length=1000, null=True, blank=True)
    Local_oil_pollution_prevention_requirements = models.CharField(max_length=1000, null=True, blank=True)
    STS_area_covered_by_oil_spill_organisation = models.CharField(max_length=1000, null=True, blank=True)
    Contract_directly_with_an_Oil_pollution_contractor = models.CharField(max_length=1000, null=True, blank=True)


class LocationsForm(forms.ModelForm):
    class Meta:
        model = Locations
        fields = [
            'name', 'fendering_position', 'Cargos_permitted',
            'Type_of_operation', 'Depth_of_water', 'Approval_to_conduct_STS_issued_by',
            'Approval_needed_prior_to_each_STS_operation', 'Vessel_sizes_permitted', 'Night_time_berthing_permitted',
            'Is_local_piloting_assistance_required', 'Local_piloting_additional_information', 'Are_tugs_required',
        ]

        help_texts = {
            'Is_local_piloting_assistance_required': _('Select yes or no'),
        }
        widgets = {
            'fendering_position': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Type_of_operation': Textarea(attrs={'cols': 50, 'rows': 1}),
            'name': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Depth_of_water': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Approval_to_conduct_STS_issued_by': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Approval_needed_prior_to_each_STS_operation': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Vessel_sizes_permitted': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Night_time_berthing_permitted': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Local_piloting_additional_information': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Are_tugs_required': Textarea(attrs={'cols': 50, 'rows': 1}),
        }


class EmergencyContactsForm(forms.ModelForm):
    class Meta:
        model = EmergencyContacts
        fields = [
            'Oil_Spill_Responders', 'Local_Emergency_Medical_Assistance', 'Police', 'Coast_Guard', 'Fire_fighting',
        ]

        widgets = {
            'Oil_Spill_Responders': Textarea(attrs={'cols': 50, 'rows': 2}),
            'Local_Emergency_Medical_Assistance': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Police': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Coast_Guard': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Fire_fighting': Textarea(attrs={'cols': 50, 'rows': 1}),
        }

class Equipment_DetailsForm(forms.ModelForm):
    class Meta:
        model = Equipment_Details
        fields = [
            'Primary_Fenders', 'Secondary_Fenders', 'Fender_Moorings', 'Rubber_Hoses', 'Composite_Hoses',
        ]

        widgets = {
            'Primary_Fenders': Textarea(attrs={'cols': 50, 'rows': 2}),
            'Secondary_Fenders': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Fender_Moorings': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Rubber_Hoses': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Composite_Hoses': Textarea(attrs={'cols': 50, 'rows': 1}),
        }


class Agent_DetailsForm(forms.ModelForm):
    class Meta:
        model = Agent_Details
        fields = [
            'Agent_Company', 'Agent_Contact', 'Fees_to_be_incurred_for_STS_Operations',
        ]

        widgets = {
            'Agent_Company': Textarea(attrs={'cols': 50, 'rows': 2}),
            'Agent_Contact': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Fees_to_be_incurred_for_STS_Operations': Textarea(attrs={'cols': 50, 'rows': 1}),
        }


class Base_DetailsForm(forms.ModelForm):
    class Meta:
        model = Base_Details
        fields = [
            'Base_Location', 'Storage_Space', 'Security_Arrangements', 'Closest_Airport', 'Local_taxi_firms',
            'Accommodation', 'Base_facilities',
        ]

        widgets = {
            'Base_Location': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Storage_Space': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Security_Arrangements': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Closest_Airport': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Local_taxi_firms': Textarea(attrs={'cols': 50, 'rows': 2}),
            'Accommodation': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Base_facilities': Textarea(attrs={'cols': 50, 'rows': 1}),
        }


class Notice_PeriodForm(forms.ModelForm):
    class Meta:
        model = Notice_Period
        fields = [
            'Notice_Period', 'Documentation_Requirements',
        ]

        widgets = {
            'Notice_Period': Textarea(attrs={'cols': 50, 'rows': 2}),
            'Documentation_Requirements': Textarea(attrs={'cols': 50, 'rows': 5}),
        }


class Support_Craft_DetailsForm(forms.ModelForm):
    class Meta:
        model = Support_Craft_Details
        fields = [
            'Vessel_Name', 'Support_Craft_Owner', 'Telephone',
        ]

        widgets = {
            'Vessel_Name': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Support_Craft_Owner': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Telephone': Textarea(attrs={'cols': 50, 'rows': 1}),
        }


class Tug_Provider_DetailsForm(forms.ModelForm):
    class Meta:
        model = Tug_Provider_Details
        fields = [
            'Tug_Provider_Company', 'Tug_Provider_Contact', 'Tug_Provider_Vessel_Name',
        ]

        widgets = {
            'Tug_Provider_Company': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Tug_Provider_Contact': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Tug_Provider_Vessel_Name': Textarea(attrs={'cols': 50, 'rows': 1}),
        }


class Area_DetailsForm(forms.ModelForm):
    class Meta:
        model = Area_Details
        fields = [
            'Location_under_the_control_of_authorities', 'Current_port_security_level',
            'What_is_considered_port_limits', 'What_is_considered_international_waters', 'Distance_from_support_base',
            'Transit_time_from_shore_to_STS_location', 'Size_of_transfer_area',
            'Does_the_area_have_a_large_enough_run_in_area', 'Is_the_transfer_area_sheltered',
            'Regulations_to_be_complied_during_the_operation', 'Nature_of_seabed', 'Average_depth_of_water',
            'STS_location_suitable_for_anchoring', 'Any_other_service_provider_in_the_same_vicinity',
        ]

        help_texts = {
            'What_is_considered_port_limits': _('Provide the complete details'),
        }
        widgets = {
            'Location_under_the_control_of_authorities': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Current_port_security_level': Textarea(attrs={'cols': 50, 'rows': 1}),
            'What_is_considered_port_limits': Textarea(attrs={'cols': 80, 'rows': 8}),
            'What_is_considered_international_waters': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Distance_from_support_base': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Transit_time_from_shore_to_STS_location': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Size_of_transfer_area': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Does_the_area_have_a_large_enough_run_in_area': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Is_the_transfer_area_sheltered': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Regulations_to_be_complied_during_the_operation': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Nature_of_seabed': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Average_depth_of_water': Textarea(attrs={'cols': 80, 'rows': 8}),
            'STS_location_suitable_for_anchoring': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Any_other_service_provider_in_the_same_vicinity': Textarea(attrs={'cols': 50, 'rows': 1}),
        }


class Navigational_HazardsForm(forms.ModelForm):
    class Meta:
        model = Navigational_Hazards
        fields = [
            'Local_marine_activity', 'Any_physical_limitations_on_vessel_size', 'Distance_from_land',
            'Any_other_navigational_hazards_in_the_area',
        ]

        widgets = {
            'Local_marine_activity': Textarea(attrs={'cols': 50, 'rows': 2}),
            'Any_physical_limitations_on_vessel_size': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Distance_from_land': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Any_other_navigational_hazards_in_the_area': Textarea(attrs={'cols': 50, 'rows': 4}),
        }


class Met_Ocean_ConditionsForm(forms.ModelForm):
    class Meta:
        model = Met_Ocean_Conditions
        fields = [
            'Prevailing_winds', 'Predominant_current', 'Average_wave_height', 'Average_swell_height_and_period',
            'What_is_the_tidal_range_if_applicable', 'Location_subject_to_restrictive_Met_conditions',
            'STS_Location_covered_by_forecasting_service',
        ]

        widgets = {
            'Prevailing_winds': Textarea(attrs={'cols': 50, 'rows': 2}),
            'Predominant_current': Textarea(attrs={'cols': 50, 'rows': 2}),
            'Average_wave_height': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Average_swell_height_and_period': Textarea(attrs={'cols': 50, 'rows': 2}),
            'What_is_the_tidal_range_if_applicable': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Location_subject_to_restrictive_Met_conditions': Textarea(attrs={'cols': 50, 'rows': 1}),
            'STS_Location_covered_by_forecasting_service': Textarea(attrs={'cols': 50, 'rows': 1}),
        }


class Environmental_DetailsForm(forms.ModelForm):
    class Meta:
        model = Environmental_Details
        fields = [
            'Location_adjacent_to_any_public_sensitive_areas', 'Environmental_bodies_to_be_advised_of_operations',
            'Local_oil_pollution_prevention_requirements', 'STS_area_covered_by_oil_spill_organisation',
            'Contract_directly_with_an_Oil_pollution_contractor',
        ]

        widgets = {
            'Location_adjacent_to_any_public_sensitive_areas': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Environmental_bodies_to_be_advised_of_operations': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Local_oil_pollution_prevention_requirements': Textarea(attrs={'cols': 50, 'rows': 1}),
            'STS_area_covered_by_oil_spill_organisation': Textarea(attrs={'cols': 50, 'rows': 1}),
            'Contract_directly_with_an_Oil_pollution_contractor': Textarea(attrs={'cols': 50, 'rows': 1}),
        }



class Entry(models.Model):
    Location_Name = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True, default='uncategorized')
    locations = models.EmbeddedModelField(
        model_container=(Locations),
        model_form_class=LocationsForm
    )

    emergencycontacts = models.EmbeddedModelField(
        model_container=(EmergencyContacts),
        model_form_class=EmergencyContactsForm
    )

    equipment_details = models.EmbeddedModelField(
        model_container=(Equipment_Details),
        model_form_class=Equipment_DetailsForm
    )

    Agent_Company = models.CharField(max_length=1000, null=True, blank=True)

    agent_details = models.EmbeddedModelField(
        model_container=(Agent_Details),
        model_form_class=Agent_DetailsForm
    )

    base_details = models.EmbeddedModelField(
        model_container=(Base_Details),
        model_form_class=Base_DetailsForm
    )

    notice_period = models.EmbeddedModelField(
        model_container=(Notice_Period),
        model_form_class=Notice_PeriodForm
    )

    support_craft_details = models.EmbeddedModelField(
        model_container=(Support_Craft_Details),
        model_form_class=Support_Craft_DetailsForm
    )

    Provider_Company = models.CharField(max_length=1000, null=True, blank=True)

    tug_provider_details = models.EmbeddedModelField(
        model_container=(Tug_Provider_Details),
        model_form_class=Tug_Provider_DetailsForm
    )

    area_details = models.EmbeddedModelField(
        model_container=(Area_Details),
        model_form_class=Area_DetailsForm
    )

    navigational_hazards = models.EmbeddedModelField(
        model_container=(Navigational_Hazards),
        model_form_class=Navigational_HazardsForm
    )

    met_ocean_conditions = models.EmbeddedModelField(
        model_container=(Met_Ocean_Conditions),
        model_form_class=Met_Ocean_ConditionsForm
    )

    environmental_details = models.EmbeddedModelField(
        model_container=(Environmental_Details),
        model_form_class=Environmental_DetailsForm
    )

    degrees_latitude = models.IntegerField(null=True, blank=True)
    minutes_latitude = models.IntegerField(null=True, blank=True)
    seconds_latitude = models.IntegerField(null=True, blank=True)
    degrees_longitude = models.IntegerField(null=True, blank=True)
    minutes_longitude = models.IntegerField(null=True, blank=True)
    seconds_longitude = models.IntegerField(null=True, blank=True)
    STS_Latitude = models.IntegerField(null=True, blank=True)
    STS_Longitude = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.STS_Latitude = int(
            self.degrees_latitude + (self.minutes_latitude / 60) + (self.seconds_latitude / 3600))
        self.STS_Longitude = int(
            self.degrees_longitude + (self.minutes_longitude / 60) + (self.seconds_longitude / 3600))
        super().save(*args, **kwargs)

    CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )

    number_of_images = models.CharField(max_length=15, null=True)
    Image1 = models.ImageField(null=True, blank=True)
    Image2 = models.ImageField(null=True, blank=True)
    Image3 = models.ImageField(null=True, blank=True)
    Image4 = models.ImageField(null=True, blank=True)
    Image5 = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_created <= now

    changed_by = models.ForeignKey('auth.User', on_delete=models.PROTECT, default='0', editable=False)
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    objects = models.DjongoManager()

    def __str__(self):
        return self.locations.name

class BlackList(models.Model):
    username = models.CharField(max_length=1000)
    flag1 = models.BooleanField(default=False)
    flag2 = models.BooleanField(default=False)
    flag3 = models.BooleanField(default=False)
    trytologintime = models.DateTimeField(auto_now_add=True, null=True)

    history = HistoricalRecords()



    def __str__(self):
        return self.username






