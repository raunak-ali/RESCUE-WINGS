from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from User.models import Profiles



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ('Name','Type_of_User','Email', 'Phone', 'Ciity', 'State', 'ID_Proof','Skill_certificates','Incentive_Expected','Experience','Type_of_disaster','Rehabilitation_Recovery_estimated_time_in_days','Service_Domain')