from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
import os
# Create your views here.


def home(requests):
    return render(requests, 'xml_translator/translator_ui.html')