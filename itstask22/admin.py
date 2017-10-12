# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

#def register(self,model_or_iterable,admin_class=None,**options):
#l=[models.HouseHolds,models.Wells,models.Yields,models.Members,models.Farms]
# Register your models here.
admin.site.register(HouseHolds)
admin.site.register(Members)
admin.site.register(Farms)
admin.site.register(Wells)
admin.site.register(Photos)
admin.site.register(Yields)

admin.site.register(Seasons)
admin.site.register(Soils)
admin.site.register(Crops)
admin.site.register(CropRequirements)
admin.site.register(Cropping)
admin.site.register(Videos)
