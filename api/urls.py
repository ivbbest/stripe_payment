from .views import *
from django.urls import path


urlpatterns = [
    path('buy/<int:pk>', BuyItemView.as_view()),
    path('buy/', BuyItemView.as_view()),
    path('item/<int:pk>', ItemView.as_view()),
]
