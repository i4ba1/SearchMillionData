from django.db.models import Q
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from zztemp_codinghw2.models import zztemp_codinghw2
from zztemp_codinghw2.serializers import zztemp_codinghw2_serializer
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def search_query(request, text):
    try:
        search_result = zztemp_codinghw2.objects. \
            filter(Q(text1__contains=text) | Q(text2__contains=text)).only('text1', 'text2').all()[:15]
        search_serializer = zztemp_codinghw2_serializer(search_result, many=True)
        return JsonResponse(search_serializer.data, safe=False)
    except zztemp_codinghw2.DoesNotExist:
        return JsonResponse({'message': 'No data found'}, status=status.HTTP_400_BAD_REQUEST)
