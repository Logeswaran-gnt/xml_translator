from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import os
# Create your views here.
class Files(APIView):
    # permission_classes = (IsAuthenticated,)             # <-- And here

    def get(self, request):
        location = request.query_params.get('path')
        # allfiles = os.listdir(r"{}".format(location))
        allfiles = os.listdir(r"D:\Banking-Domain\banking\api")
        xmlfiles = [f for f in allfiles if f.endswith('xml')]
        return Response(xmlfiles)
