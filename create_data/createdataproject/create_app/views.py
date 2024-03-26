import io

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt #providing external csrf token

@csrf_exempt
def Studnet_Create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {
                'msg': 'Data Created'
            }
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        # if there will be error

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
