from .views import *
from django.urls import path


urlpatterns = [
    # path('api/v1/buy/', ItemView.as_view()),
    path('buy/', test_payment),

    # path('api/v1/item/<int>:id', item, name='item'),
]
