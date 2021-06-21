
import pandas as pd
from rest_framework import serializers

from Intelligence.models import Prediction
# from ..models import Intelligence


class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ['id','n','pred','image']
