from django.db import models
from django.utils import timezone

# Create your models here.
class Facility(models.Model):
    facilityname = models.CharField(max_length=250,null=False, unique="facility_name")
    rateperhour = models.FloatField()
    capacity = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now, editable=False, null=False)
    modified_at = models.DateTimeField(default=timezone.now, null=False)

    def save(self, *args, **kwargs):
        # Update the modified_at timestamp whenever the object is saved
        self.modified_at = timezone.now()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.facilityname
    
class Setting_Facility(models.Model):
    facility = models.CharField(max_length=100,null=False, )
    mainrules = models.CharField(max_length=100,null=False)
    promorules = models.CharField(max_length=100,null=False)
    subrules = models.CharField(max_length=100,null=False)
    
    created_at = models.DateTimeField(default=timezone.now, editable=False, null=False)
    modified_at = models.DateTimeField(default=timezone.now, null=False)

    def save(self, *args, **kwargs):
        # Update the modified_at timestamp whenever the object is saved
        self.modified_at = timezone.now()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.facility
    

class Facility_MainRules(models.Model):
    facility = models.CharField(max_length=100,null=True,default=None)
    title = models.CharField(max_length=100,null=False, unique="title")
    points = models.FloatField(blank=False, default=0.00)
    num_pc = models.IntegerField(blank=False, default=0)
    num_attendies = models.IntegerField(blank=False)
    description = models.CharField(max_length=255,null=False)
    rate = models.IntegerField(blank=False, default=0)
    status = models.BooleanField(default=0)

    created_at = models.DateTimeField(default=timezone.now, editable=False, null=False)
    modified_at = models.DateTimeField(default=timezone.now, null=False)

    def save(self, *args, **kwargs):
        # Update the modified_at timestamp whenever the object is saved
        self.modified_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Facility_MainRules_set(models.Model):
    facility = models.CharField(max_length=100,null=True,default=None)
    title = models.CharField(max_length=100,null=False)
    points = models.FloatField(blank=False, default=0.00)
    num_pc = models.IntegerField(blank=False, default=0)
    num_attendies = models.IntegerField(blank=False, default=0)
    description = models.CharField(max_length=255,null=False, default="")
    rate = models.IntegerField(blank=False, default=0)
    status = models.BooleanField(default=0)

    created_at = models.DateTimeField(default=timezone.now, editable=False, null=False)
    modified_at = models.DateTimeField(default=timezone.now, null=False)

    def save(self, *args, **kwargs):
        # Update the modified_at timestamp whenever the object is saved
        self.modified_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title    
    
class Facility_SubRules(models.Model):
    facility = models.CharField(max_length=100, null=True, default=None)
    title = models.CharField(max_length=100,null=False)
    description = models.CharField(max_length=100,null=False)
    status = models.BooleanField(default=0)

    created_at = models.DateTimeField(default=timezone.now, editable=False, null=False)
    modified_at = models.DateTimeField(default=timezone.now, null=False)

    def save(self, *args, **kwargs):
        # Update the modified_at timestamp whenever the object is saved
        self.modified_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title  

class Facility_SubRules_set(models.Model):
    facility = models.CharField(max_length=100, null=True, default=None)
    title = models.CharField(max_length=100,null=False)
    description = models.CharField(max_length=100,null=False)
    status = models.BooleanField(default=0)

    created_at = models.DateTimeField(default=timezone.now, editable=False, null=False)
    modified_at = models.DateTimeField(default=timezone.now, null=False)

    def save(self, *args, **kwargs):
        # Update the modified_at timestamp whenever the object is saved
        self.modified_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title 


class Facility_PromoRules(models.Model):
    facility = models.CharField(max_length=100, null=True, default=None)
    title = models.CharField(max_length=100,null=False)
    description = models.CharField(max_length=100,null=False)
    status = models.BooleanField(default=0)
    new_rate = models.FloatField(blank=False, default=0.00)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    capacity = models.IntegerField(default=0)

    created_at = models.DateTimeField(default=timezone.now, editable=False, null=False)
    modified_at = models.DateTimeField(default=timezone.now, null=False)

    def save(self, *args, **kwargs):
        # Update the modified_at timestamp whenever the object is saved
        self.modified_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title    

class Facility_PromoRules_set(models.Model):
    facility = models.CharField(max_length=100, null=True, default=None)
    title = models.CharField(max_length=100,null=False)
    description = models.CharField(max_length=100,null=False)
    status = models.BooleanField(default=0)
    new_rate = models.FloatField(blank=False, default=0.00)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    capacity = models.IntegerField(default=0)

    created_at = models.DateTimeField(default=timezone.now, editable=False, null=False)
    modified_at = models.DateTimeField(default=timezone.now, null=False)

    def save(self, *args, **kwargs):
        # Update the modified_at timestamp whenever the object is saved
        self.modified_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title  
    
class Revenue_Transaction(models.Model):
    transaction_date = models.DateTimeField(null=False)
    facility = models.CharField(max_length=100, null=True, default=None)
    facility_fee = models.FloatField(default=0.00)
    event_name = models.CharField(max_length=100,null=False)
    customer_name = models.CharField(max_length=100,null=False)
    num_attendies = models.IntegerField(default=0)
    start_date = models.DateTimeField(null=False)
    end_date = models.DateTimeField(null=False)
    payment = models.FloatField(default=0.00)
    attendie_name = models.CharField(max_length=100,null=False)
    time_in = models.DateTimeField(null=False)
    time_out = models.DateTimeField(null=False)
    charge_payment = models.FloatField(default=0.00)

    created_at = models.DateTimeField(default=timezone.now, editable=False, null=False)
    modified_at = models.DateTimeField(default=timezone.now, null=False)
    
    def __str__(self):
        return self.facility 



# from django.db import models

# class DatePreference(models.Model):
#     DAY_CHOICES = [
#         ('monday', 'Monday'),
#         ('tuesday', 'Tuesday'),
#         ('wednesday', 'Wednesday'),
#         ('thursday', 'Thursday'),
#         ('friday', 'Friday'),
#         ('saturday', 'Saturday'),
#         ('sunday', 'Sunday'),
#     ]

#     selected_days = models.CharField(max_length=50, choices=DAY_CHOICES)
#     every_day = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Every {self.selected_days}" if self.every_day else self.selected_days

    

