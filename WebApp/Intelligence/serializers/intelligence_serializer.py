
import pandas as pd
from rest_framework import serializers

from Intelligence.models import Predictions
# from ..models import Intelligence


class PredictionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predictions
        fields = ['id','n','pred','image']
