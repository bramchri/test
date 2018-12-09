from django.db import models


class BusinessData(models.Model):
    city = models.CharField(max_length=250,  blank=True, null=True, verbose_name=u'city')
    holderName = models.CharField(max_length=250,  blank=True, null=True, verbose_name=u'holderName')
    isNonRemitted = models.IntegerField( blank=True, null=True, verbose_name=u'isNonRemitted')
    ownerName = models.CharField(max_length=250,  blank=True, null=True, verbose_name=u'ownerName')
    postalCode = models.CharField(max_length=250,  blank=True, null=True, verbose_name=u'postalCode')
    propertyID = models.IntegerField( blank=True, null=True, verbose_name=u'propertyID')
    propertyTypeDescription = models.CharField(max_length=250,  blank=True, null=True,  verbose_name=u'propertyTypeDescription')
    propertyValue = models.FloatField( blank=True, null=True, verbose_name=u'propertyValue')
    propertyValueDescription = models.CharField(max_length=250,  blank=True, null=True,  verbose_name=u'propertyValueDescription')
    secondOwnerName = models.CharField(max_length=250,  blank=True, null=True,  verbose_name=u'secondOwnerName')
    swsPropertyID = models.IntegerField( blank=True, null=True,  verbose_name=u'swsPropertyID', unique=True)
    siteID = models.ForeignKey('SiteModel',blank=True, null=True, on_delete=models.CASCADE)
    is_imported = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)


class Dictionary(models.Model):
    name = models.CharField(max_length=125,  blank=True, null=True, verbose_name=u'name')


class SiteModel(models.Model):
    url = models.CharField(max_length=250)
    name = models.CharField(max_length=250)

class LastId(models.Model):
    number = models.IntegerField(default=0)