# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from django.http import HttpResponse
from itstask22.models import *
from .serializers import *

class AgroList(APIView):
	def get(self,request):
		h=HouseHolds.objects.all()
		h1=AgroSerializer(h,many=True)
		return Response(h1.data)
	def post(self):
		pass

class FarmList(APIView):
	def get(self,request):
		h=Farms.objects.all()
		h1=FarmSerializer(h,many=True)
		return Response(h1.data)
	def post(self):
		pass

class WellList(APIView):
        def get(self,request):
                h=Wells.objects.all()
                h1=WellSerializer(h,many=True)
                return Response(h1.data)
        def post(self):
                pass
class VideoList(APIView):
	def get(self,request):
		h=Videos.objects.all()
		h1=VideoSerializer(h,many=True)
		return Response(h1.data)
	def post(self):
		pass
class MemberList(APIView):
        def get(self,request):
                h=Members.objects.all()
                h1=MemberSerializer(h,many=True)
                return Response(h1.data)
        def post(self):
                pass
class PhotoList(APIView):
        def get(self,request):
                h=Photos.objects.all()
                h1=PhotoSerializer(h,many=True)
                return Response(h1.data)
        def post(self):
                pass

class YieldList(APIView):
        def get(self,request):
                h=Yields.objects.all()
                h1=YieldSerializer(h,many=True)
                return Response(h1.data)
        def post(self):
                pass
class CropRequirementsList(APIView):
        def get(self,request):
                h=CropRequirements.objects.all()
                h1=CropRequirementsSerializer(h,many=True)
                return Response(h1.data)
        def post(self):
                pass
class CroppingList(APIView):
        def get(self,request):
                h=Cropping.objects.all()
                h1=CroppingSerializer(h,many=True)
                return Response(h1.data)
        def post(self):
                pass
