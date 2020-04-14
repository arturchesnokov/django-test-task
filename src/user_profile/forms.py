from django import forms
from django.forms import DateInput
from user_profile.models import User


# 7. forms-model-extra - (edit profile form has been done with forms.ModelForm
class CustomUserChangeForm(forms.ModelForm):
    # 6. forms-widgets - assign calendar widget to "date of birth" field.
    date_of_birth = forms.DateField(
        widget=DateInput(attrs={
            'type': 'date',
            'class': 'datepicker'
        }
        ))

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'date_of_birth',
            'biography',
            'contacts',
        )
