import time

import pandas as pd
from django.contrib.auth.models import User
from rest_framework import serializers


class IntelligenceSerializer(serializers.ModelSerializer):
    class Meta:
        # model = Accommodation
        fields = ['id','landlord','name','type',
        'period', 'baths', 'address','included', 'rules', 'payment_methods']


