from rdb.models import DuplexFrequencyPair,Repeater
from rest_framework import serializers



class DFPSerializer(serializers.ModelSerializer):
    class Meta:
        model = DuplexFrequencyPair
        fields = '__all__'


class RepeaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repeater
        fields = '__all__'