from django.contrib import messages
from django.contrib.auth.models import User
from .models import Payment
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.http import JsonResponse
from .forms import CustomUserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.utils import timezone
from datetime import timedelta

# API to return recent payment stats
def api_stats(request):
    values = list(Payment.objects.order_by('-timestamp').values_list('amount', flat=True)[:5])
    return JsonResponse({'values': values[::-1]})

# Home view (not restricted)
def home_view(request):
    return render(request, 'admin/custom_admin_dashboard.html')

# Custom dashboard (login required, not staff-only)
@login_required
def custom_admin_dashboard(request):
    user_count = User.objects.count()
    total_payments = Payment.objects.aggregate(Sum('amount'))['amount__sum'] or 0
    recent_users = User.objects.order_by('-date_joined')[:5]

    return render(request, 'admin/custom_admin_dashboard.html', {
        'user_count': user_count,
        'total_payments': total_payments,
        'recent_users': recent_users,
    })

# Registration view
def register_view(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard:custom_admin_dashboard')
    else:
        form = CustomUserForm()

    return render(request, 'registration/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:custom_admin_dashboard')
        else:
            return render(request, 'registration/login.html', {'error_message': 'Invalid username or password.'})
    
    return render(request, 'registration/login.html')

# Optional: You can use Django's built-in login view if you want
class CustomLoginView(auth_views.LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('dashboard:custom_admin_dashboard')


@login_required
def users_view(request):
    # Fetch all users from the User model
    users = User.objects.all()  # Fetch all users
    return render(request, 'admin/users.html', {'users': users})

@login_required
def authorization_view(request):
    users = User.objects.all()  # Get all users

    if request.method == 'POST':
        # Iterate through each user and update their role
        for user in users:
            role = request.POST.get(f'role_{user.id}')
            if role:
                user_id = request.POST.get(f'user_id_{user.id}')
                user = User.objects.get(id=user_id)

                # Update role based on selected value
                if role == 'admin':
                    user.is_staff = True
                    user.is_superuser = True
                elif role == 'staff':
                    user.is_staff = True
                    user.is_superuser = False
                else:
                    user.is_staff = False
                    user.is_superuser = False

                user.save()  # Save the updated user


        return redirect('dashboard:authorization')  # Redirect after update to show success message

    return render(request, 'admin/authorization.html', {'users': users})

@login_required
def report_view(request):
    total_users = User.objects.count()
    staff_count = User.objects.filter(is_staff=True, is_superuser=False).count()
    admin_count = User.objects.filter(is_superuser=True).count()
    recent_users = User.objects.filter(date_joined__gte=timezone.now()-timedelta(days=7))

    return render(request, 'admin/report.html', {
        'total_users': total_users,
        'staff_count': staff_count,
        'admin_count': admin_count,
        'recent_users': recent_users
    })


@login_required
def logout_view(request):
    logout(request)
    return redirect('dashboard:login')

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def grant_role(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_staff = True
    user.save()
    return redirect('dashboard:authorization')

@user_passes_test(lambda u: u.is_superuser)
def revoke_role(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_staff = False
    user.save()
    return redirect('dashboard:authorization')
