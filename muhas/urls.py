from django.urls import path
from .views import *

urlpatterns = [
    path('home/', index_view, name='home'),
    path('welcome/', welcome_view, name="welcome"),
    path('select/', select_view, name="select"),
    path('preview/', preview_view, name="preview"),
    path('data/', data_received, name='data'),
]
