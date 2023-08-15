from django import forms
from django.core import validators
from forms_app.models import User

# You can make your own validators, for instance, we
# will create a validator that checks if the name starts
# wit a Z:

def check_for_z(value): # The argument named "value" is mandatory
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name must start with Z") 

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z]) # Then we need to add the validator to the name field
    email = forms.EmailField()
    # Verifying the email
    verify_email = forms.EmailField(label='Verify your email:')
    text = forms.CharField(widget=forms.Textarea)

    ## Adding hidden inputs
    # Adding a check for a bot
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
    
    '''
    # This is an example, but pretty much you will never validate a form this way.
    # However, you can sustitute all this code with the validators=[validators.MaxLengthValidator(0)] line above.

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError('Gotcha Bot!')
        return botcatcher
    '''

    # Clean all data at once
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Emails doesn't match!")

## This is the form model

class NewUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'