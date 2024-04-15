from django.shortcuts import redirect, render
from .forms import loginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse("Invalid input")
    else:
        form = loginForm()
    return render(request, 'users/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html')


@login_required
def index(request):
    return render(request, 'users/index.html')
