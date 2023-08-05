from django.urls import path
from .views import *

app_name='config'
urlpatterns = [
    path('links/', LinkView.as_view(), name='links')
]