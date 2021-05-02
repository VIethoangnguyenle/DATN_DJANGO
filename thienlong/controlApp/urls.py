from django.contrib import admin
from django.urls import path
from .views import control,submitData,sendmail,filterDay, loginSite
urlpatterns = [
    path('', loginSite.as_view(), name = 'login'),
    path('control/',control, name = 'control'),
    path('api/control/',submitData),
    path('api/filter/',filterDay),
    path('api/sendmail/',sendmail),
]
