from rest_framework import serializers
from .models import RouterDetails
#from django.db import transaction

class RouterSerializer(serializers.ModelSerializer):

	class Meta:
		model = RouterDetails
		fields = '__all__'