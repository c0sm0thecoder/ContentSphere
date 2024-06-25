from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.http import HttpResponse

from .forms import CustomUserCreationForm


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print(form.is_valid())
        print("errors:", form.errors)
        if form.is_valid():
            form.save()
            return redirect('login', form.cleaned_data['email'], form.cleaned_data['password1'])
    else:
        form = CustomUserCreationForm()
    return HttpResponse("Invalid form")


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("Invalid login")
    return HttpResponse("Invalid login")
