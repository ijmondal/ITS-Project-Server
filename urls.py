from django.conf.urls import url,include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from itstask22 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^agrohouseholds/',views.AgroList.as_view()),
    url(r'^agrofarms/',views.FarmList.as_view()),
    url(r'^agrowells/',views.WellList.as_view()),    
    url(r'^agroyields/',views.YieldList.as_view()),
    url(r'^agrocroprequirment/',views.CropRequirementList.as_view()),
    url(r'^agrocropping/',views.CroppingList.as_view()),
    url(r'^maps/', include('itstask22.urls'))
]
urlpatterns=format_suffix_patterns(urlpatterns)
