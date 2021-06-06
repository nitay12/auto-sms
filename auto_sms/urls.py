from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('sms/', include('sms.urls')),
    path('admin/', admin.site.urls),
    ]
