from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Multi Purpose Vendor"
admin.site.site_title = "ONLY ADMIN"
admin.site.index_title = "Welcome To apni Dukaan"

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
]
