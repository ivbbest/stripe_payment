from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import ItemSerializer

from .models import Item
import stripe

stripe.api_key = "sk_test_51L04RSBzb84rnJEJtIUz2CkTwd072wXv21bTdiYaaQIG4eoqxmCYQTpOqrS9BeokLnFN5SvoYDNFNu7z4lPwbuxY00bW1dwIgH"


# class ItemView(APIView):
#     def post(self, request):
#         stripes.api_key = "sk_test_51L04RSBzb84rnJEJtIUz2CkTwd072wXv21bTdiYaaQIG4eoqxmCYQTpOqrS9BeokLnFN5SvoYDNFNu7z4lPwbuxY00bW1dwIgH"
#
#         stripes.Price.create(
#             currency="usd",
#             unit_amount=120000,
#             product_data={"name": "stand up paddleboard"},
#         )
#
#     # def get(self, request, id):
#     #     pass


# @api_view(['POST'])
# def test_payment(request):
#     test_payment_intent = stripe.Price.create(
#         currency="usd",
#         unit_amount=120000,
#         product_data={"name": "stand up paddleboard"},
#     )
#
#     return Response(status=status.HTTP_200_OK, data=test_payment_intent)

class ItemView(APIView):
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        # breakpoint()
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            info = serializer.data
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': info['name'],
                            'description': info['description']
                        },
                        'unit_amount': info['price']*100,
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url='http://127.0.0.1:8000/',
                cancel_url='http://127.0.0.1:8000/',
            )

            return Response({'sessionId': session['id']}, status=status.HTTP_201_CREATED)
            # return Response({'sessionId': session['id']})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        item = get_object_or_404(Item, pk=pk)
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                        'description': item.description
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:8000/',
            cancel_url='http://127.0.0.1:8000/',
        )

        # pay_data = {
        #     "price_data": {
        #         "currency": "usd",
        #         "unit_amount": 1,
        #         "product_data": {
        #             "name": item.name,
        #             'description': item.description,
        #             'price': item.price
        #         }
        #     },
        #     "quantity": 1,
        # }
        #
        # session = stripe.checkout.Session.create(
        #     success_url='http://127.0.0.1:8000/',
        #     cancel_url='http://127.0.0.1:8000/',
        #     payment_method_types=['card'],
        #     mode='payment',
        #     line_items=[
        #         pay_data,
        #     ]
        # )

        data = {'session_id': session.id}

        return Response(status=status.HTTP_200_OK, data=data)

# @api_view(['GET', 'POST'])
# def buy_item(request, item_pk=None):
# item = get_object_or_404(Item, pk=item_pk)
# pay_data = {
#     "price_data": {
#         "currency": "usd",
#         "unit_amount": 1000,
#         "product_data": {
#             "name": item.name,
#             'description': item.description,
#             'price': item.price
#         }
#     },
#     "quantity": 1,
# }
#
# session = stripe.checkout.Session.create(
#     success_url='http://127.0.0.1:8000/',
#     cancel_url='http://127.0.0.1:8000/',
#     payment_method_types=['card'],
#     mode='payment',
#     line_items=[
#         pay_data,
#     ]
# )
#
# data = {'session_id': session.id}
#
# return Response(status=status.HTTP_200_OK, data=data)


# @api_view(['GET'])
# def get_item(request, item_pk):
#     item = get_object_or_404(Item, pk=item_pk)
#     return render(request, 'Stripe/get_item.html', {'item': item})
