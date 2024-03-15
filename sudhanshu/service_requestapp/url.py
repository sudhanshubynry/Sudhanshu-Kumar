# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_service_request, name='submit_service_request'),
    path('success/', views.success_page, name='success_page'),
]


# project_name/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('service/', include('app_name.urls')),
]
