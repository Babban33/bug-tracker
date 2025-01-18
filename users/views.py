from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    if user.role == 'admin':
        return render(request, 'users/admin_dashboard.html')
    elif user.role == 'developer':
        return render(request, 'users/developer_dashboard.html')
    else:  # tester
        return render(request, 'users/tester_dashboard.html')