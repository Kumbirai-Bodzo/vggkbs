from django.conf import settings
from django.conf.urls import handler404, url
from django.contrib import admin
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.core.mail import send_mail
from django.urls import include, path, re_path
from django.views.generic import RedirectView, TemplateView

from . import views

urlpatterns = [
  path('post', views.IntelligenceView.as_view(), name='intelligence'),
  path('get', views.IntelligenceView.as_view(), name='intelligence'),
]

