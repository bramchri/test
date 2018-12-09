from django.urls import path
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns

from storage.views import MainView, BDViewSet, DictionarySet, DictionaryDetail, LastIdView


urlpatterns = [
    path('^$', MainView.as_view()),
    path('admin/', admin.site.urls),
    path('api/v1/save-data/', BDViewSet.as_view()),
    path('api/v1/dictionary/', DictionarySet.as_view()),
    path('api/v1/dictionary/<int:pk>/', DictionaryDetail.as_view()),
    path('api/v1/last_id/<int:pk>/', LastIdView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
