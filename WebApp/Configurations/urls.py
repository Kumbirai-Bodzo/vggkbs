from django.conf import settings
from django.conf.urls import handler404, url
from django.contrib import admin
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.core.mail import send_mail
from django.urls import include, path, re_path
from django.views.generic import RedirectView, TemplateView

urlpatterns = [

    path('admin/', admin.site.urls),
   path('api/intelligence/', include('Intelligence.urls')),
  #  path('api/shared/', include('Shared.urls')), 
  #  path('api/auth/', include('Authentication.urls')),
  #  path('api/accommodation/', include('Accommodation.urls')),
   # path('api/transport/', include('Transport.urls')),
   # path('', include('Shop.urls')),  
    
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)

urlpatterns += [
re_path(r'^(?P<path>.*)$', TemplateView.as_view(template_name='angular.html'), name="home"),
   # url(r'^.*', TemplateView.as_view(template_name='angular.html'), name="home"),
  # url(r'^.*', TemplateView.as_view(template_name='angular.html'), name="home"),
]


'''subject = 'Some subject'
from_email = settings.CUSTOM_DEFAULT_FROM_EMAIL
message = 'This is my test message'
recipient_list = ['bodzok@gmail.com']
html_message = '<h1>This is my HTML test</h1>'''

# send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)
# handler404 = vf.serve_angular
