<<<<<<< HEAD
from django import forms
from .models import UserInfo
class UserProfileForm(forms.Form):
    employment = forms.CharField(max_length = 20, widget=forms.TextInput, required = False,  help_text="<br>")
    location = forms.CharField(max_length = 50, widget = forms.TextInput(attrs={'placeholder':'Enter your location.'}), required = False, help_text = "<br>")
    birthday = forms.CharField(max_length = 50, widget = forms.TextInput(attrs={'placeholder':'yyyy-mm-dd'}), required = False, help_text = "<br>")
    interest = forms.CharField(max_length = 50,widget = forms.TextInput(attrs={'placeholder':'Enter your interest'}), required = False)

    def clean(self):
        cleaned_data = super(UserProfileForm, self).clean()
        employment = cleaned_data.get('employment')
        location = cleaned_data.get('location')
        birthday = cleaned_data.get('birthday')
        interest = cleaned_data.get('interest')
        if not employment and not location and not birthday:
            raise forms.ValidationError('You have to write something!')

=======
from django import forms
from .models import UserInfo
class UserProfileForm(forms.Form):
    employment = forms.CharField(max_length = 20, widget=forms.TextInput, required = False,  help_text="<br>")
    location = forms.CharField(max_length = 50, widget = forms.TextInput(attrs={'placeholder':'Enter your location.'}), required = False, help_text = "<br>")
    birthday = forms.CharField(max_length = 50, widget = forms.TextInput(attrs={'placeholder':'yyyy-mm-dd'}), required = False, help_text = "<br>")
    interest = forms.CharField(max_length = 50,widget = forms.TextInput(attrs={'placeholder':'Enter your interest'}), required = False)

    def clean(self):
        cleaned_data = super(UserProfileForm, self).clean()
        employment = cleaned_data.get('employment')
        location = cleaned_data.get('location')
        birthday = cleaned_data.get('birthday')
        interest = cleaned_data.get('interest')
        if not employment and not location and not birthday:
            raise forms.ValidationError('You have to write something!')

>>>>>>> project03
    