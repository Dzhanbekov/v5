from django.urls import path
from .views import *

urlpatterns = [
    path('', index.as_view(), name='home'),
    path('about/', About.as_view(), name='about')
]