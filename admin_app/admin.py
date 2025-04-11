from django.contrib.admin import AdminSite


class CustomAdminSite(AdminSite):
    site_header = 'Authentication Admin'
    site_title = 'Custom Admin Dashboard'
    index_title = 'Welcome to Custom Admin'
admin_site = CustomAdminSite(name='custom_admin')

