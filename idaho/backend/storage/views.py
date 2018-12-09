import json

from django.http import Http404
from django.views.generic.base import TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Dictionary, SiteModel, LastId
from .serializers import BusinessDataSerializer, DictSerializer


class MainView(TemplateView):
    template_name = "index.html"


class BDViewSet(APIView):

    parser_classes = tuple()
    permission_classes = tuple()

    def get(self, request, format=None):
        return Response([])

    def post(self, request, format=None):
        req = json.loads(request.body.decode('utf-8'))
        data = json.loads(req['resp'])['properties']
        site = req['site']
        site_obj = SiteModel.objects.get_or_create(url=site.split('https://')[1])

        if len(data) == 0:
            return Response([])
        for i in data:
            i['siteID'] = site_obj[0].id
            a = BusinessDataSerializer(data=i)
            if a.is_valid():
                a.create(validated_data=a.validated_data)
        return Response([])


class DictionarySet(APIView):

    def get(self, request, format=None):
        names = Dictionary.objects.all()
        serializer = DictSerializer(names, many=True)
        nameDict = {}
        for i in serializer.data:
            nameDict[i['name']] = 1
        return Response(nameDict)

    def post(self, request, format=None):
        return Response('None')


class DictionaryDetail(APIView):

    def get_object(self, pk):
        try:
            return Dictionary.objects.get(pk=pk)
        except Dictionary.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = DictSerializer(snippet)
        return Response(serializer.data)


class LastIdView(APIView):
    def get(self, request, pk, format=None):
        record = LastId.objects.get_or_create(id=pk)
        return Response(record[0].number)

    def post(self, request, pk, format=None):
        record = LastId.objects.get_or_create(id=pk)
        record[0].number = json.loads(request.body.decode('utf-8'))
        record[0].save()
        return Response([])