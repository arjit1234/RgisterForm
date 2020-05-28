from django import forms


class RegisterForm(forms.Form):
    first_name=forms.CharField(
        label='Enter Your First Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your first Name'
                }
            )
        )
    last_name=forms.CharField(
        label='Enter Your Last Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'pllcaholder':'Your Last Name'
                }
            )
        )
    username=forms.CharField(
        label='Enter Your Username',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Username'
                }
            )
        )
    password=forms.CharField(
        label='Enter Yoour Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Password'
                }
            )
        )
    mobile=forms.IntegerField(
        label='Enter Your Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Mobile Number'
                }
            )
        )


class LoginForm(forms.Form):
    username=forms.CharField(
        label='Enter Your Username',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Username'
                }
            )
        )
    password=forms.CharField(
        label='Enter Your Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Password'
                }
            )
        )