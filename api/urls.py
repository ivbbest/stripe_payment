from .views import *
from django.urls import path


urlpatterns = [
    # path('api/v1/buy/', ItemView.as_view()),
    # path('test/', test_payment),
    path('buy/<int:pk>', ItemView.as_view()),
    path('buy/', ItemView.as_view()),
    # path('item/<int:item_pk>', get_item),

    # path('api/v1/item/<int>:id', item, name='item'),
]
