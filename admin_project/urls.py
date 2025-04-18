"""admin_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from admin_app.views import custom_admin_dashboard, login_view, register_view

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('dashboard', include('admin_app.urls')),
    path('register/', register_view, name='register'),
    path('', login_view, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', include('admin_app.urls', namespace='admin')),

]
