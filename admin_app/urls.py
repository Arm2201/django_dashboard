from django import views
from django.urls import path
from .views import (
    grant_role, home_view, register_view, login_view, custom_admin_dashboard, 
    api_stats, revoke_role, users_view, authorization_view, report_view, logout_view
)

app_name = 'dashboard'

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('custom-dashboard/', custom_admin_dashboard, name='custom_admin_dashboard'),
    path('users/', users_view, name='users'),
    path('authorization/', authorization_view, name='authorization'),
    path('grant_role/<int:user_id>/', grant_role, name='grant_role'),
    path('revoke_role/<int:user_id>/', revoke_role, name='revoke_role'),
    path('reports/', report_view, name='reports'),
    path('api/stats/', api_stats, name='api_stats'),
]
