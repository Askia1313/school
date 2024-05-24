from django.contrib import admin
from . import views
from django.urls import path, include

app_name = 'account'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('APP1/', include('APP1.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

]
