from django import forms
from django.forms import ModelForm

from .models import Facility, Facility_MainRules, Facility_MainRules_set, Facility_PromoRules, Facility_PromoRules_set, Facility_SubRules, Facility_SubRules_set, Revenue_Transaction, Setting_Facility

class FacilityForm(ModelForm):
    facilityname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Facility Name'}))
    rateperhour = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Enter rate per hour'}))
    capacity = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter Capacity'}))

    class Meta:
        model = Facility
        fields = ['facilityname', 'rateperhour', 'capacity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def clean(self):
        cleaned_data = super().clean()
        facilityname = cleaned_data.get('facilityname')
        rateperhour = cleaned_data.get('rateperhour')
        capacity = cleaned_data.get('capacity')

        if rateperhour is not None and rateperhour < 10:
            self.add_error('rateperhour', 'Rate per hour should not be below 10.')

        if capacity is not None and capacity > 30:
            self.add_error('capacity', 'Capacity should not exceed 30.')
        
        if Facility.objects.filter(facilityname=facilityname).exclude(pk=self.instance.pk).exists():
            self.add_error('facilityname', 'Facility with this name already exists.')


        return cleaned_data

    def __str__(self):
        return self.cleaned_data['facilityname'] + " ( " + str(self.cleaned_data['rateperhour']) + ") " + " (" + str(self.cleaned_data['capacity']) + ") "

class FacilityUpdateForm(ModelForm):
    facilityname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Facility Name'}))
    rateperhour = forms.FloatField(widget=forms.TextInput(attrs={'placeholder':'Enter rate per hour'}))
    capacity = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Enter Capacity'}))

    class Meta:
        model = Facility
        fields = ['facilityname', 'rateperhour', 'capacity']

    def clean(self):
        cleaned_data = super().clean()
        facilityname = cleaned_data.get('facilityname')
        rateperhour = cleaned_data.get('rateperhour')
        capacity = cleaned_data.get('capacity')

        if rateperhour is not None and rateperhour < 10:
            self.add_error('rateperhour', 'Rate per hour should not be below 10.')

        if capacity is not None and capacity > 30:
            self.add_error('capacity', 'Capacity should not exceed 30.')
        
        if Facility.objects.filter(facilityname=facilityname).exclude(pk=self.instance.pk).exists():
            self.add_error('facilityname', 'Facility with this name already exists.')


        return cleaned_data

    # def __str__(self):
    #     return self.cleaned_data['facilityname'] + " ( " + str(self.cleaned_data['rateperhour']) + ") " + " (" + str(self.cleaned_data['capacity']) + ") "


    def __init__(self, *args, **kwargs):
        super(FacilityUpdateForm, self).__init__(*args, **kwargs)

        # Set placeholders for the form fields
        self.fields['facilityname'].widget.attrs['placeholder'] = 'Rate Per Hour'
        self.fields['rateperhour'].widget.attrs['placeholder'] = 'Rate Per Hour'
        self.fields['capacity'].widget.attrs['placeholder'] = 'Capacity'        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['facilityname'].initial = False

class SettingFacilityUpdateForm(ModelForm):
    facility = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Facility'}))
    mainrules = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Main Rules'}))
    promorules = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Promo Rules'}))
    subrules = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Sub Rules'}))

    class Meta:
        model = Setting_Facility
        fields = ['facility','mainrules','promorules','subrules']

class SettingFacilityForm(ModelForm):
    facility = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Facility'}))
    mainrules = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Main Rules'}))
    promorules = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Promo Rules'}))
    subrules = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Sub Rules'}))

    class Meta:
        model = Setting_Facility
        fields = ['facility','mainrules','promorules','subrules']

class EditFacilityForm(ModelForm):
    facility = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Facility'}))
    mainrules = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Main Rules'}))
    promorules = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Promo Rules'}))
    subrules = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Sub Rules'}))

    class Meta:
        model = Setting_Facility
        fields = ['facility','mainrules','promorules','subrules']

class FacilityForm(ModelForm):
    facilityname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Facility Name'}))
    rateperhour = forms.FloatField(widget=forms.TextInput(attrs={'placeholder':'Enter rate per hour'}))
    capacity = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Enter Capacity'}))

    class Meta:
        model = Facility
        fields = ['facilityname','rateperhour','capacity']

    def __str__(self):
        return self.facilityname+ " (" +self.rateperhour +") "+" (" +self.capacity +") "

class FacilityTable(ModelForm):
    facilityname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Facility Name'}))
    rateperhour = forms.FloatField(widget=forms.TextInput(attrs={'placeholder':'Enter rate per hour'}))
    capacity = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Enter Capacity'}))

    class Meta:
        model = Facility
        fields = ['facilityname','rateperhour','capacity']

class UpdateFacilityForm(ModelForm):
    facilityname = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Facility Name'}))
    rateperhour = forms.FloatField(widget=forms.TextInput(attrs={'placeholder':'Enter rate per hour'}))
    capacity = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Enter Capacity'}))

    class Meta:
        model = Facility
        fields = ['id','facilityname','rateperhour','capacity']

    def __str__(self):
        return self.id+ " (" +self.facilityname+ " (" +self.rateperhour +") "+" (" +self.capacity +") "

# Add Main Rules to the User Form
class FacilityMainRulesForm(ModelForm):
    # facility = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add Title'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add Title'}))
    points = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Points consumption per week'}))
    num_pc = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Number of PC Facility can book'}))
    num_attendies = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Number of person can attend'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    rate = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Rate per person'}))
    # status = forms.BooleanField()
    class Meta:
        model = Facility_MainRules
        fields = ['title','points','num_pc','num_attendies','description','rate']
        exclude = ['status','facility']  

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['status'].initial = False  # Set 'status' field's initial value to False (0)

class UpdateFacilityMainRulesForm(ModelForm):
    facility = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add Title'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add Title'}))
    points = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Points consumption per week'}))
    num_pc = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Number of PC Facility can book'}))
    num_attendies = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Number of person can attend'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    rate = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Rate per person'}))
    status = forms.BooleanField()
    class Meta:
        model = Facility_MainRules
        fields = ['facility','title','points','num_pc','num_attendies','description','rate','status']

    def clean(self):
        cleaned_data = super().clean()
        facility = cleaned_data.get('facility')
        title = cleaned_data.get('title')

        # Check if a record with the same title and facility exists
        existing_record = Facility_MainRules_set.objects.filter(facility=facility, title=title).first()

        if existing_record:
            # If facility and title combination already exists, raise a validation error
            if self.instance and self.instance.pk == existing_record.pk:
                # If editing the existing record, allow the same combination
                return cleaned_data
            self.add_error('title', 'A record with this Facility and Title combination already exists.')

        return cleaned_data

    def __str__(self):
        return (
            f"{self.cleaned_data['facility']} ({self.cleaned_data['title']}) "
            f"({self.cleaned_data['rate']} per person) "
            f"({self.cleaned_data['capacity']})"
        )

class FacilityMainRulesSetForm(ModelForm):
    facility = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add Title'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add Title'}))
    points = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Points consumption per week'}))
    num_pc = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Number of PC Facility can book'}))
    num_attendies = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Number of person can attend'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    rate = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Rate per person'}))
    status = forms.BooleanField()
    class Meta:
        model = Facility_MainRules_set
        fields = ['facility','title','points','num_pc','num_attendies','description','rate','status']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['status'].initial = False  # Set 'status' field's initial value to False (0)





class FacilitySubRulesForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add Title'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    
    class Meta:
        model = Facility_SubRules  # Use '=' instead of ':'
        fields = ['title', 'description']
        exclude = ['status', 'facility']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['status'].initial = False

class FacilitySubRulesSetForm(ModelForm):
    facility = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add Title'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add Title'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    status = forms.BooleanField()

    class Meta:
        model = Facility_SubRules_set
        fields = ['facility','title','description','status']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['status'].initial = False  # Set 'status' field's initial value to False (0)

class FacilityPromoRulesForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add Title'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    new_rate = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Enter new rate'}))
    start_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placehodler': 'Start date'}))
    end_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placehodler': 'End date'}))
    capacity = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter Capacity'}))
 
    class Meta:
        model = Facility_PromoRules  # Use '=' instead of ':'
        fields = ['title', 'description','new_rate','start_date', 'end_date', 'capacity']
        exclude = ['status', 'facility']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['status'].initial = False


class FacilityPromoRulesSetForm(ModelForm):
    facility = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add Title'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add Title'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    new_rate = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder':'Enter new rate'}))
    start_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placehodler': 'Start date'}))
    end_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placehodler': 'End date'}))
    capacity = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter Capacity'}))
    status = forms.BooleanField()

    class Meta:
        model = Facility_PromoRules_set
        fields = ['facility','title','description','new_rate','start_date', 'end_date', 'capacity','status']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['status'].initial = False  # Set 'status' field's initial value to False (0)

class Revenue_TransactionForm(ModelForm):
    transaction_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placehodler': 'Start date'}))
    facility = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add Title'}))
    event_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add Title'}))
    customer_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add Title'}))
    num_attendies = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter Capacity'}))
    start_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placehodler': 'Start date'}))
    end_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placehodler': 'Start date'}))
    attendie_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add Title'}))
    time_in = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placehodler': 'Start date'}))
    time_out = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placehodler': 'Start date'}))
    charge_payment = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placehodler': 'Start date'}))

    class Meta:
        model = Revenue_Transaction
        fields = ['transaction_date', 'facility','facility_fee','payment',
                  'event_name', 'customer_name', 'num_attendies',
                  'start_date', 'end_date', 'attendie_name', 'time_in',
                  'time_out','charge_payment']


