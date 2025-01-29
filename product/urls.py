from django.urls import path
from product import views
urlpatterns = [
    path('list/',views.Listapi.as_view(),name='list'),
    path('laptop/',views.Laptopapi.as_view(),name='create'),
    path('mobile/',views.Mobileapi.as_view(),name='update'),
    path('topwear/',views.Topwearapi.as_view(),name='topwear'),
    path('buttomwear/',views.Buttomwearapi.as_view(),name='buttomwear'),
]
