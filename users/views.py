from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import RegistrationForm, UserLoginForm



def account_register(request):

    registerForm = RegistrationForm()

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            print(registerForm.cleaned_data)
            user = registerForm.save(commit=False)
            user.set_password(registerForm.cleaned_data['password'])
            user.save()
            return redirect('account:login')

    return render(request, 'blog/registration.html', {'form': registerForm})




def login_user(request):
    form = UserLoginForm()
    if request.method == 'POST':
        login_form = UserLoginForm(data=request.POST)
        print(login_form.is_valid())
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Email yoki parol xato!')
            return redirect('account:login')


    content = {
        'form': form,
        'next': next,
    }

    return render(request, 'blog/login.html', content)





def logout_view(request):
    logout(request)
    return redirect('/')
