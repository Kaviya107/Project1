from django import forms
from .models import *

class basic_details_form(forms.ModelForm):
    class Meta:
        model = basic_details
        fields=['firstname','lastname','mobile_number','DOB','email_address','gender']
        widgets={

            'firstname':forms.TextInput(attrs={'class':'form-control','placeholder':'firstname'}),
            'lastname':forms.TextInput(attrs={'class':'form-control','placeholder':'lastname'}),
            'email_address':forms.TextInput(attrs={'class':'form-control','placeholder':'email_address'}),
            'mobile_number':forms.TextInput(attrs={'class':'form-control','placeholder':'mobile_number'}),
            'DOB':forms.DateInput(format=('%d-%m-%Y'),attrs={'type':'date','class': 'form-control'}),
            'gender':forms.RadioSelect(choices=gender_choices,attrs={}),
        }
class others_form(forms.ModelForm):
    class Meta:
        model = other_details
        fields=['father_name','mother_name','address','city','pincode','aadhar_number','driving_license','emergency_contact_name','emergency_contact_number']
        widgets={
            'father_name':forms.TextInput(attrs={'class':'form-control','placeholder':'father_name'}),
            'mother_name':forms.TextInput(attrs={'class':'form-control','placeholder':'mother_name'}),
            'address':forms.Textarea(attrs={'class':'form-control','placeholder':'address' ,'rows':'5'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'city'}),
            'pincode':forms.TextInput(attrs={'class':'form-control','placeholder':'pincode'}),
            'aadhar_number':forms.TextInput(attrs={'class':'form-control','placeholder':'aadhar_number'}),
            'driving_license':forms.TextInput(attrs={'class':'form-control','placeholder':'license_number'}),
            'emergency_contact_name':forms.TextInput(attrs={'class':'form-control','placeholder':'emergency_contact_name'}),
            'emergency_contact_number':forms.TextInput(attrs={'class':'form-control','placeholder':'emergency_contact_number'}),

        }
class designation_details_form(forms.ModelForm):
    class Meta:
        model = designation_details
        fields=['designation','salary','date_of_join']
        widgets={
            'designation':forms.TextInput(attrs={'class':'form-control','placeholder':'designation'}),
            'salary':forms.TextInput(attrs={'class':'form-control','placeholder':'salary'}),
            'date_of_join':forms.DateInput(format=('%d-%m-%Y'),attrs={'type':'date','class': 'form-control'}),
        }

class salary_details_form(forms.ModelForm):
    class Meta:
        model = salary_details
        fields=['account_number','IFSC_code','bank_name','bank_address']
        widgets={
            'account_number':forms.TextInput(attrs={'class':'form-control','placeholder':'account_number'}),
            'IFSC_code':forms.TextInput(attrs={'class':'form-control','placeholder':'IFSC_code'}),
            'bank_name':forms.TextInput(attrs={'class':'form-control','placeholder':'bank_name'}),
            'bank_address':forms.TextInput(attrs={'class':'form-control','placeholder':'bank_address'}),
        }