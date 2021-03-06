from django import forms
#from django.db import models
from Donor.models import Donor,Donation
from django.core.exceptions import ValidationError
import re

class NewDonorForm(forms.ModelForm):
    def clean_age(self):
        data=self.cleaned_data['age']
        if data>70:
            raise ValidationError(('You are gonna die soon'))
        if data<18:
            raise ValidationError(('Too young to donate blood'))
        return data
        
    def clean_phone(self):
        data=self.cleaned_data['phone']
        reg="^(\d{10})$"
        if len(data)==10 and re.search(reg, data):
            print("valid")
        else:
            raise ValidationError(('Mobile Number must have 10 digits'))
        return data

    def clean_donorId(self):
        data=self.cleaned_data['donorId']
        reg="^[a-zA-Z0-9_-]*$"
        if re.search(reg, data):
            print("valid")
        else:
            raise ValidationError(('ID can only contain alphanumeric chars., underscore and hyphen!'))
        return data

    class Meta:
        model=Donor
        fields= ('donorId','name','address','phone','email','age','sex','bloodType')

class NewDonationForm(forms.ModelForm):
    class Meta:
        model=Donation
        fields= ('donorId','quantity')