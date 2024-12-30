from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='core-page'),
    path('<str:id>/', get_chatbot_by_id, name='cbot')
]