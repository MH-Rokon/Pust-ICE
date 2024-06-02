from django.contrib.auth.forms import UserCreationForm
from django import forms
from .constants import ACCOUNT_TYPE
from django.contrib.auth.models import User
from .models import UserAccount, UserDepartment

class UserRegistrationForm(UserCreationForm):
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE)
    roll_number = forms.IntegerField(required=True)
    registration_no = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'account_type', 'roll_number', 'registration_no']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            account_type = self.cleaned_data.get('account_type')
            roll_number = self.cleaned_data.get('roll_number')
            registration_no = self.cleaned_data.get('registration_no')

            UserAccount.objects.create(
                user=user,
                account_type=account_type,
                roll_number=roll_number,
                registration_no=registration_no
            )

        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })

class UserUpdateForm(forms.ModelForm):
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE)
    roll_number = forms.IntegerField(required=False)
    registration_no = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'account_type', 'roll_number', 'registration_no']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })
        if self.instance:
            try:
                user_account = self.instance.account
            except UserAccount.DoesNotExist:
                user_account = None

            if user_account:
                self.fields['account_type'].initial = user_account.account_type
                self.fields['roll_number'].initial = user_account.roll_number
                self.fields['registration_no'].initial = user_account.registration_no

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_account, created = UserAccount.objects.get_or_create(user=user)

            user_account.account_type = self.cleaned_data['account_type']
            user_account.roll_number = self.cleaned_data.get('roll_number')
            user_account.registration_no = self.cleaned_data.get('registration_no')
            user_account.save()

        return user
