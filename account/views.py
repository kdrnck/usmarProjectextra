from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


from .forms import RegistrationForm, UserEditForm
from .models import UserBase

@login_required
def dashboard(request):
    return render(request,
            'account/user/dashboard.html')

def account_register(request):

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = True
            user.save()

            return redirect('account:dashboard')
    else:
        registerForm = RegistrationForm()
    return render(request, 'account/registration/register.html', {'form': registerForm})

@login_required
def delete_user(request):
    if request.method == 'post':
        user = UserBase.objects.get(user_name=request.user)
        user.is_active = False
        user.save()
        logout(request)
    return redirect('account:delete_confirmation')

@login_required
def edit_details(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)

    return render(request,
                    'account/user/edit_details.html', {'user_form': user_form})

