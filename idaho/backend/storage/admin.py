from django.contrib import admin

from storage.models import BusinessData, Dictionary


class BusinessDataAdmin(admin.ModelAdmin):
    list_display = ('ownerName', 'holderName', 'city', 'postalCode', 'propertyValueDescription')
    search_fields = ('ownerName', 'holderName', 'city', 'postalCode', 'propertyValueDescription')


class DictionaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Dictionary, DictionaryAdmin)
admin.site.register(BusinessData, BusinessDataAdmin)
