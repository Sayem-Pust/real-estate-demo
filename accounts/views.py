from django.shortcuts import render, redirect


def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect('index')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')

    return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
