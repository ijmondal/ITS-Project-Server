from rest_framework import serializers
from itstask22.models import *

class AgroSerializer(serializers.ModelSerializer):
	class Meta:
		model=HouseHolds
		fields='__all__'


class FarmSerializer(serializers.ModelSerializer):
	class Meta:
		model=Farms
		fields='__all__'

class WellSerializer(serializers.ModelSerializer):
        class Meta:
                model=Wells
                fields='__all__'

class PhotoSerializer(serializers.ModelSerializer):
        class Meta:
                model=Photos
                fields='__all__'
class VideoSerializer(serializers.ModelSerializer):
        class Meta:
                model=Videos
                fields='__all__'

class MemberSerializer(serializers.ModelSerializer):
        class Meta:
                model=Members
                fields='__all__'

class YieldSerializer(serializers.ModelSerializer):
        class Meta:
                model=Yields
                fields='__all__'

class CropRequirementsSerializer(serializers.ModelSerializer):
        class Meta:
                model=CropRequirements
                fields='__all__'

class CroppingSerializer(serializers.ModelSerializer):
        class Meta:
                model=Cropping
                fields='__all__'

