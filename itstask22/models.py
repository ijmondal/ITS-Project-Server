
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry
from decimal import Decimal
import datetime


class HouseHolds(models.Model):
	ID=models.IntegerField(primary_key=True)
	Monthly_Income=models.FloatField(null=True, blank=True, default=300.00)
	Location_Id=models.PointField(default = 'POINT( 13.222713 79.110090 )')
	#HeadOfHousehold=models.ForeignKey('Members')
	#Photo_Id=models.ForeignKey('Photos', defaultl)
	def __str__(self):
		return str(self.ID)
	
class Members(models.Model):
	ID=models.IntegerField(primary_key=True)
	HouseHold_Id=models.ForeignKey('HouseHolds',on_delete=models.CASCADE,default=1)
	Name=models.CharField(max_length=10)
	DOB=models.DateTimeField()
	Gender=models.CharField(max_length=1)
	Photo_Id=models.ForeignKey('Photos',on_delete=models.CASCADE,null=True,blank=True, default = 1)
	def __str__(self):
                return str(self.Name)

        
class Farms(models.Model):
	ID=models.IntegerField(primary_key=True)
	Area=models.DecimalField(max_digits=90,decimal_places=5)
	Points=models.PolygonField()
	HouseHold_Id=models.ForeignKey('HouseHolds',on_delete=models.CASCADE,default=1)
	Soil_Id=models.ForeignKey('Soils',default=1)
       

class Wells(models.Model):
	ID=models.IntegerField(primary_key=True)
	Depth=models.DecimalField(max_digits=20,decimal_places=5)
	Location_Id = models.PointField(default = 'POINT(79.110090 13.222713)')
	Photo_Id=models.ForeignKey('Photos',on_delete=models.CASCADE,null=True)
        def __str__(self):
                return str(self.ID)


class Yields(models.Model):
	ID = models.IntegerField(primary_key = True)
	Well_Id = models.ForeignKey('Wells',on_delete=models.CASCADE,default=1)
        Yield_Measure = models.DecimalField(max_digits=20,decimal_places=5)
        Time= models.DateTimeField()
	class Meta:
		unique_together=(('Well_Id','Time'),)
        def __str__(self):
                return str(self.ID)


class Photos(models.Model):
	ID=models.IntegerField(primary_key=True)
	Photo=models.ImageField()
	def __str__(self):
                return str(self.ID)

       
class Videos(models.Model):
	ID = models.IntegerField(primary_key = True)
	Video_Clip = models.CharField(max_length = 100)
	Household_Id = models.ForeignKey('HouseHolds', default = 1)
	def __str__(self):
                return str(self.ID)


class Seasons(models.Model):
	ID=models.IntegerField(primary_key=True)
	Season=models.CharField(max_length=20)
        def __str__(self):
                return str(self.ID)

       
class Soils(models.Model):
	ID=models.IntegerField(primary_key=True)
	Soil=models.CharField(max_length=20)
        def __str__(self):
                return str(self.ID)

        

class CropRequirements(models.Model):
	#ID = models.IntegerField(primary_key = True)
	Crop_Id=models.ForeignKey('Crops')
	Season_Id=models.ForeignKey('Seasons')
	Soil_Id=models.ForeignKey('Soils', default = 1)
	Fertility=models.DecimalField(default=1.0,max_digits=20,decimal_places=5)
	Moisture_Content=models.DecimalField(default=1.0,max_digits=20,decimal_places=5)
	class Meta:
		unique_together=(('Crop_Id','Season_Id'),)


class Crops(models.Model):
	ID=models.IntegerField(primary_key=True)
	Name=models.CharField(max_length=50)
        def __str__(self):
                return str(self.ID)


class Cropping(models.Model):
	Year=models.IntegerField()
	Farm_Id=models.ForeignKey('Farms',null=True)
	Crop_Id=models.ForeignKey('Crops',null=True)
	Photo_Id=models.ForeignKey('Photos',null=True)
	Season_Id=models.ForeignKey('Seasons',default=1)
        def __str__(self):
                return str(self.ID)


