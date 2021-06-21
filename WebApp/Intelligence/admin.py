from Configurations.auto_create_super_user import *
from django.contrib import admin

from Intelligence.models import Prediction

# Register your models here.
admin.site.register(Prediction)
