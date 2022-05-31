from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItemSerializer
from payment.config import STRIPE_SECRET_KEY

from .models import Item
import stripe


stripe.api_key = STRIPE_SECRET_KEY


class ItemView(APIView):
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
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

        data = {'session_id': session.id}

        return Response(status=status.HTTP_200_OK, data=data)
