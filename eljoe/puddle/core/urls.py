from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from . import views
from .forms import Loginform
from django.conf import settings
from django.conf.urls.static import static


app_name = 'core'

urlpatterns = [
    path('', views.index),
    path('contact/', views.contact, name="contact"),
    path('signup/', views.signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='static/login.html', authentication_form=Loginform), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)