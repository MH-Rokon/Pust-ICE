from django.contrib.auth import login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, UpdateView
from .forms import UserRegistrationForm, UserUpdateForm

class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        # Retrieve roll and registration from form data
        roll = form.cleaned_data.get('roll_number')
        registration = form.cleaned_data.get('registration_no')

        # Check if both roll and registration are provided
        if roll is not None and registration is not None:
            # Validate the roll and registration
            if validate_roll_and_registration(roll, registration):
                # If valid, proceed with registration
                user = form.save()
                login(self.request, user)
                messages.success(self.request, 'Registration successful. You are now logged in.')
                return super().form_valid(form)
            else:
                # If not valid, display error message and return invalid form
                messages.error(self.request, 'Invalid roll or registration. Please try again.')
                return self.form_invalid(form)

        # If roll or registration is missing, display error message and return invalid form
        messages.error(self.request, 'Please enter both roll and registration numbers.')
        return self.form_invalid(form)
    
def validate_roll_and_registration(roll, registration):
    # Check if roll and registration are integers
    try:
        roll = int(roll)
        registration = int(registration)
    except ValueError:
        return False

  
    expected_registration = roll + 864765
   
    
    # Check if registration matches the expected value
    if registration == expected_registration:
        return True
    
    return False


class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    success_url = reverse_lazy('home')

def user_logout(request):
    logout(request)
    return redirect(reverse_lazy('login')) 

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/profile.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user
