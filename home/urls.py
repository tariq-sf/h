
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home_list),
    path('all',views.home_detail),
]
