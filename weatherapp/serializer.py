from rest_framework import serializers
from .models import *


###################### RegistrationInfo Serializer Start ######################
class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'