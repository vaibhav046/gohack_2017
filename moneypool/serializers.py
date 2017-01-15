from rest_framework import serializers
from .models import Masterprofile,Profile,Transaction


class MasterprofileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Masterprofile
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'

