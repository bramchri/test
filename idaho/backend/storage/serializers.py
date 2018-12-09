from rest_framework import serializers

from .models import BusinessData, Dictionary


class BusinessDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessData
        fields = (
            'city',
            'holderName',
            'isNonRemitted',
            'ownerName',
            'postalCode',
            'propertyID',
            'propertyTypeDescription',
            'propertyValue',
            'propertyValueDescription',
            'secondOwnerName',
            'swsPropertyID',
            'siteID'
        )


class DictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields =(
            'name',
        )
