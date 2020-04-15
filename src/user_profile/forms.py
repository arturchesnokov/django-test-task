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


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    date_of_birth = forms.DateField(
        widget=DateInput(attrs={'type': 'date', 'class': 'datepicker'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2', 'date_of_birth')

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password'] != cleaned_data['password2']:
                raise forms.ValidationError('Passwords not equal!')
        return cleaned_data

    def save(self, commit=True):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = True
        user.save()
        return user
