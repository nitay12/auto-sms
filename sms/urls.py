from django.urls import path

from . import views
app_name = 'sms'
urlpatterns = [
    path('', views.form, name='form'),
    path('send/', views.send, name='send'),
]