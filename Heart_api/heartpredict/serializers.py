from rest_framework import serializers

from heartpredict.models import info

class InfoSerializer(serializers.ModelSerializer):

    class Meta: 
        model = info
        fields = ('male', 'BPMeds', 'prevalentStroke', 'prevalentHyp', 'diabetes', 'log_cigsPerDay', 'log_totChol', 'log_diaBP', 'log_BMI', 'log_heartRate', 'log_glucose', 'log_age')
