from django.urls import path
from .views import *

urlpatterns = [
    
    path('people/',PeopleAPI.as_view()),
    path('children/',children),
]
